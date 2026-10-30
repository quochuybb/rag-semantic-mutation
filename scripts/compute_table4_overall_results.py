"""
Reproduce Table 4: Summary of RAG Evaluation Results Across Five Configurations
(2,080 Total Runs from 832 Mutated Documents) and Human Validation (N=210).

Paper Reference:
- main_iciit.tex: Table 4 (tab:results) & Section 3.4 (Evaluation Pipeline and Metrics)
- main.tex: Table 4 (tab:results) & Section 3.4 (Data Analysis and Evaluation Metrics)
"""

import os
import sys
import pandas as pd
import numpy as np

def cohen_kappa(y1, y2):
    y1, y2 = np.array(y1), np.array(y2)
    categories = np.unique(np.concatenate([y1, y2]))
    n = len(y1)
    if n == 0:
        return 0.0, 0.0, 0.0
    po = np.mean(y1 == y2)
    pe = sum(np.mean(y1 == c) * np.mean(y2 == c) for c in categories)
    if pe == 1.0:
        return po, 1.0, 0.0
    kappa = (po - pe) / (1.0 - pe)
    # Standard error of Cohen's Kappa
    se = np.sqrt(po * (1.0 - po) / (n * (1.0 - pe)**2)) if (1.0 - pe) > 0 else 0.0
    return po, kappa, se

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    configs = [
        {
            'name': 'Llama 4 Scout 17B (With Prompt, Public Data)',
            'ai_file': os.path.join(repo_root, 'llama-3.1-17b-prompt', 'results', 'ai_judgements.csv'),
            'h_file': os.path.join(repo_root, 'llama-3.1-17b-prompt', 'results', 'human_eval_sample_new.csv'),
        },
        {
            'name': 'Llama 4 Scout 17B (Without Prompt, Public Data)',
            'ai_file': os.path.join(repo_root, 'llama-3.1-17b-noprompt', 'results', 'ai_judgements_new.csv'),
            'h_file': os.path.join(repo_root, 'llama-3.1-17b-noprompt', 'results', 'human_eval_sample_new.csv'),
        },
        {
            'name': 'Llama 3.1 8B (With Prompt, Public Data)',
            'ai_file': os.path.join(repo_root, 'llama-3.1-8b-prompt', 'results', 'ai_judgements_new.csv'),
            'h_file': os.path.join(repo_root, 'llama-3.1-8b-prompt', 'results', 'human_eval_sample_new.csv'),
        },
        {
            'name': 'Llama 3.1 8B (Without Prompt, Public Data)',
            'ai_file': os.path.join(repo_root, 'llama-3.1-8b-noprompt', 'results', 'ai_judgements_new.csv'),
            'h_file': os.path.join(repo_root, 'llama-3.1-8b-noprompt', 'results', 'human_eval_sample_new.csv'),
        },
        {
            'name': 'Llama 4 Scout 17B (With Prompt, Private Data)',
            'ai_file': os.path.join(repo_root, 'data_private', 'results', 'ai_judge_llama4.csv'),
            'h_file': os.path.join(repo_root, 'data_private', 'results', 'human_eval_sample_new.csv'),
        },
    ]

    print("=" * 105)
    print("TABLE 4: SUMMARY OF RAG EVALUATION RESULTS ACROSS FIVE CONFIGURATIONS (N = 2,080 RUNS)")
    print("=" * 105)
    header = f"{'Model Configuration':<46} | {'Kappa':<7} | {'Abstain':<8} | {'Faithful':<8} | {'Inconsistent':<12} | {'Hallucination':<13}"
    print(header)
    print("-" * 105)

    all_human = []
    all_ai = []

    for cfg in configs:
        df_ai = pd.read_csv(cfg['ai_file'])
        df_h = pd.read_csv(cfg['h_file'])

        tot = len(df_ai)
        counts = df_ai['ai_label'].str.strip().value_counts()
        abstain = counts.get('Abstain', 0) / tot * 100
        faithful = counts.get('Faithful', 0) / tot * 100
        inconsistent = counts.get('Inconsistent', 0) / tot * 100
        hallucination = counts.get('Hallucination', 0) / tot * 100

        if 'ai_label' in df_h.columns:
            y_h = df_h['human_label'].str.strip()
            y_a = df_h['ai_label'].str.strip()
        else:
            merged = pd.merge(df_h[['mut_id', 'human_label']], df_ai[['mut_id', 'ai_label']], on='mut_id')
            y_h = merged['human_label'].str.strip()
            y_a = merged['ai_label'].str.strip()

        po, k, se = cohen_kappa(y_h, y_a)
        print(f"{cfg['name']:<46} | {k:0.3f}   | {abstain:6.2f}% | {faithful:6.2f}% | {inconsistent:10.2f}% | {hallucination:11.2f}%")

        all_human.extend(y_h.tolist())
        all_ai.extend(y_a.tolist())

    print("-" * 105)
    all_human = np.array(all_human)
    all_ai = np.array(all_ai)
    po_tot, k_tot, se_tot = cohen_kappa(all_human, all_ai)
    ci_low = max(0.0, k_tot - 1.96 * se_tot)
    ci_high = min(1.0, k_tot + 1.96 * se_tot)
    agreed = np.sum(all_human == all_ai)
    n_val = len(all_human)

    print("\nHUMAN VALIDATION AUDIT (STRATIFIED SAMPLE N = 210, 42 PER CONFIGURATION):")
    print(f"  - Total Human Validation Instances: {n_val}")
    print(f"  - Observed Raw Agreement: {agreed}/{n_val} ({po_tot * 100:.2f}%)")
    print(f"  - Overall Cohen's Kappa: \u03ba = {k_tot:.3f} (Standard Error = {se_tot:.3f})")
    print(f"  - 95% Confidence Interval: [{ci_low:.3f}, {ci_high:.3f}]")
    print("=" * 105)

if __name__ == '__main__':
    main()
