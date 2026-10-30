"""
Reproduce Table 7 (Sensitivity Analysis: One-Sided Exact Binomial Tests of Abstain Rates
Across Operational Benchmarks).

Paper Reference:
- main_iciit.tex: Table 7 (tab:sensitivity_benchmarks) & Section 4.2
- main.tex: Table 12 (tab:binom_summary) & Section 4.7
"""

import os
import sys
import pandas as pd
from scipy.stats import binomtest

def clopper_pearson_ci(k, n, confidence=0.95):
    res = binomtest(k=k, n=n)
    ci = res.proportion_ci(confidence_level=confidence)
    return ci.low, ci.high

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    configs = [
        {
            'name': '17B With Prompt (Public)',
            'file': os.path.join(repo_root, 'llama-3.1-17b-prompt', 'results', 'ai_judgements.csv')
        },
        {
            'name': '17B Without Prompt (Public)',
            'file': os.path.join(repo_root, 'llama-3.1-17b-noprompt', 'results', 'ai_judgements_new.csv')
        },
        {
            'name': '8B With Prompt (Public)',
            'file': os.path.join(repo_root, 'llama-3.1-8b-prompt', 'results', 'ai_judgements_new.csv')
        },
        {
            'name': '8B Without Prompt (Public)',
            'file': os.path.join(repo_root, 'llama-3.1-8b-noprompt', 'results', 'ai_judgements_new.csv')
        },
        {
            'name': '17B With Prompt (Private)',
            'file': os.path.join(repo_root, 'data_private', 'results', 'ai_judge_llama4.csv')
        }
    ]

    print("=" * 115)
    print("TABLE 7: SENSITIVITY ANALYSIS: ONE-SIDED EXACT BINOMIAL TESTS OF ABSTAIN RATES (N = 416)")
    print("=" * 115)
    header = f"{'Configuration':<28} | {'Count (k/N)':<11} | {'Abstain (%)':<11} | {'95% Clopper CI':<19} | {'p vs. 50%':<10} | {'p vs. 75%':<11} | {'p vs. 90%':<11}"
    print(header)
    print("-" * 115)

    for cfg in configs:
        df = pd.read_csv(cfg['file'])
        N = len(df)
        k = int((df['ai_label'].str.strip() == 'Abstain').sum())
        rate = k / N * 100
        
        ci_low, ci_high = clopper_pearson_ci(k, N, 0.95)
        
        # One-sided tests: H0: p >= p0 vs H1: p < p0
        p_50 = binomtest(k, N, p=0.50, alternative='less').pvalue
        p_75 = binomtest(k, N, p=0.75, alternative='less').pvalue
        p_90 = binomtest(k, N, p=0.90, alternative='less').pvalue

        def format_p(p):
            if p >= 0.001:
                return f"{p:.3f}"
            else:
                return f"{p:.2e}"

        ci_str = f"[{ci_low*100:5.2f}%, {ci_high*100:5.2f}%]"
        cnt_str = f"{k}/{N}"
        rate_str = f"{rate:6.2f}%"

        print(f"{cfg['name']:<28} | {cnt_str:<11} | {rate_str:<11} | {ci_str:<19} | {format_p(p_50):<10} | {format_p(p_75):<11} | {format_p(p_90):<11}")

    print("=" * 115)

if __name__ == '__main__':
    main()
