"""
Reproduce Table 8: Confusion Matrix Between Independent Human Evaluator and LLM Judge
(N = 210, kappa = 0.858, 90.95% observed agreement).

Paper Reference:
- main_iciit.tex: Table 8 (tab:judge_confusion) & Section 5.3
- main.tex: Table 10 (tab:judge_confusion) & Section 5.3
"""

import os
import sys
import pandas as pd
import numpy as np

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    configs = [
        ('17B With Prompt (Public)', os.path.join(repo_root, 'llama-3.1-17b-prompt', 'results', 'human_eval_sample_new.csv'), os.path.join(repo_root, 'llama-3.1-17b-prompt', 'results', 'ai_judgements.csv')),
        ('17B Without Prompt (Public)', os.path.join(repo_root, 'llama-3.1-17b-noprompt', 'results', 'human_eval_sample_new.csv'), os.path.join(repo_root, 'llama-3.1-17b-noprompt', 'results', 'ai_judgements_new.csv')),
        ('8B With Prompt (Public)', os.path.join(repo_root, 'llama-3.1-8b-prompt', 'results', 'human_eval_sample_new.csv'), os.path.join(repo_root, 'llama-3.1-8b-prompt', 'results', 'ai_judgements_new.csv')),
        ('8B Without Prompt (Public)', os.path.join(repo_root, 'llama-3.1-8b-noprompt', 'results', 'human_eval_sample_new.csv'), os.path.join(repo_root, 'llama-3.1-8b-noprompt', 'results', 'ai_judgements_new.csv')),
        ('17B With Prompt (Private)', os.path.join(repo_root, 'data_private', 'results', 'human_eval_sample_new.csv'), os.path.join(repo_root, 'data_private', 'results', 'ai_judge_llama4.csv')),
    ]

    all_rows = []
    for name, h_f, ai_f in configs:
        df_h = pd.read_csv(h_f)
        df_ai = pd.read_csv(ai_f)
        if 'ai_label' in df_h.columns:
            df_sub = df_h[['mut_id', 'human_label', 'ai_label']].copy()
        else:
            df_sub = pd.merge(df_h[['mut_id', 'human_label']], df_ai[['mut_id', 'ai_label']], on='mut_id')
        df_sub['config'] = name
        all_rows.append(df_sub)

    df_all = pd.concat(all_rows, ignore_index=True)
    df_all['human_label'] = df_all['human_label'].str.strip()
    df_all['ai_label'] = df_all['ai_label'].str.strip()

    labels = ['Abstain', 'Faithful', 'Inconsistent', 'Hallucination']
    cm = pd.crosstab(df_all['human_label'], df_all['ai_label'], rownames=['Human'], colnames=['Judge']).reindex(index=labels, columns=labels, fill_value=0)

    print("=" * 80)
    print("TABLE 8: CONFUSION MATRIX BETWEEN INDEPENDENT HUMAN EVALUATOR AND LLM JUDGE (N = 210)")
    print("=" * 80)
    print(cm)
    print("-" * 80)

    total_n = len(df_all)
    agreed = (df_all['human_label'] == df_all['ai_label']).sum()
    disagreed = total_n - agreed
    raw_agreement = agreed / total_n * 100

    # Categorize disagreements
    f_inc = ((df_all['human_label'] == 'Faithful') & (df_all['ai_label'] == 'Inconsistent')).sum() + \
            ((df_all['human_label'] == 'Inconsistent') & (df_all['ai_label'] == 'Faithful')).sum()
    abs_f = ((df_all['human_label'] == 'Abstain') & (df_all['ai_label'] == 'Faithful')).sum() + \
            ((df_all['human_label'] == 'Faithful') & (df_all['ai_label'] == 'Abstain')).sum()
    inc_hal = ((df_all['human_label'] == 'Inconsistent') & (df_all['ai_label'] == 'Hallucination')).sum() + \
              ((df_all['human_label'] == 'Hallucination') & (df_all['ai_label'] == 'Inconsistent')).sum()

    print(f"Total Validation Samples: {total_n}")
    print(f"Agreement: {agreed}/{total_n} ({raw_agreement:.2f}%)")
    print(f"Disagreements: {disagreed}/{total_n} ({disagreed/total_n*100:.2f}%)")
    print(f"\nDisagreement Error Mode Breakdown:")
    print(f"  1. Faithful vs. Inconsistent: {f_inc}/{disagreed} ({f_inc/disagreed*100:.1f}%)")
    print(f"  2. Abstain vs. Faithful:      {abs_f}/{disagreed} ({abs_f/disagreed*100:.1f}%)")
    print(f"  3. Inconsistent vs. Halluc:   {inc_hal}/{disagreed} ({inc_hal/disagreed*100:.1f}%)")
    print("=" * 80)

if __name__ == '__main__':
    main()
