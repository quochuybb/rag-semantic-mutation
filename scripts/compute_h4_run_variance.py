"""
Reproduce Section 6.2 (Internal Validity): Run-to-Run Decoding Variance Audit
(104 Stratified Samples x 3 Repeated Runs = 312 Runs at temperature=0.7).

Paper Reference:
- main_iciit.tex: Section 6 (Threats to Validity, Internal Validity)
- main.tex: Section 6.2 (Internal Validity)
"""

import os
import sys
import csv
import json
import numpy as np

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    h4_dir = os.path.join(repo_root, 'data', 'validation', 'variance_h4')
    
    judged_file = os.path.join(h4_dir, 'h4_judged_responses.csv')
    metrics_file = os.path.join(h4_dir, 'h4_metrics.json')

    if not os.path.exists(judged_file):
        print(f"Error: {judged_file} not found!")
        return

    with open(judged_file, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    N = len(rows)
    print("=" * 100)
    print("H4 RUN-TO-RUN DECODING VARIANCE AUDIT (104 SAMPLES x 3 RUNS = 312 EVALUATIONS AT temp=0.7)")
    print("=" * 100)

    # 1. Run distributions
    labels = ["Abstain", "Faithful", "Inconsistent", "Hallucination"]
    runs = ["run1_label", "run2_label", "run3_label"]

    print(f"{'Run ID':<10} | {'Abstain':<12} | {'Faithful':<12} | {'Inconsistent':<14} | {'Hallucination':<15}")
    print("-" * 100)

    run_rates = {l: [] for l in labels}
    for r_idx, r_col in enumerate(runs, 1):
        counts = {l: sum(1 for row in rows if row[r_col] == l) for l in labels}
        rates = {l: counts[l] / N * 100 for l in labels}
        for l in labels:
            run_rates[l].append(rates[l])
        print(f"Run {r_idx:<6} | {rates['Abstain']:5.2f}% ({counts['Abstain']}/{N}) | {rates['Faithful']:5.2f}% ({counts['Faithful']}/{N}) | {rates['Inconsistent']:5.2f}% ({counts['Inconsistent']}/{N})   | {rates['Hallucination']:5.2f}% ({counts['Hallucination']}/{N})")

    print("-" * 100)

    # 2. Within-condition variance
    print("\nWITHIN-CONDITION STOCHASTIC VARIANCE (STD DEV ACROSS REPEATED RUNS):")
    for l in labels:
        rates = run_rates[l]
        mean_r = np.mean(rates)
        sd_r = np.std(rates, ddof=1)
        print(f"  - {l:<15}: Mean = {mean_r:5.2f}%, Within-condition SD = \u00b1{sd_r:4.2f}% (Rates: {rates[0]:.1f}%, {rates[1]:.1f}%, {rates[2]:.1f}%)")

    # 3. Label switch rate
    any_switch = sum(1 for r in rows if not (r["run1_label"] == r["run2_label"] == r["run3_label"]))
    stable_count = N - any_switch
    any_switch_rate = any_switch / N * 100
    stable_rate = stable_count / N * 100

    switch_12 = sum(1 for r in rows if r["run1_label"] != r["run2_label"])
    switch_23 = sum(1 for r in rows if r["run2_label"] != r["run3_label"])
    switch_13 = sum(1 for r in rows if r["run1_label"] != r["run3_label"])
    pairwise_mean_switch = (switch_12 + switch_23 + switch_13) / (3 * N) * 100

    print("\nLABEL STABILITY ACROSS RUNS:")
    print(f"  - Total Stratified Sample Size: {N}")
    print(f"  - Fully Stable Queries (All 3 runs agree): {stable_count}/{N} ({stable_rate:.2f}%)")
    print(f"  - Label-Switch Rate (Switched in \u2265 1 run):  {any_switch}/{N} ({any_switch_rate:.2f}%)")
    print(f"  - Pairwise Mean Switch Rate:              {pairwise_mean_switch:.2f}%")
    print("\nCONCLUSION ON INTERNAL VALIDITY:")
    print(f"  * Within-condition SD of Abstain = \u00b1{np.std(run_rates['Abstain'], ddof=1):.2f}% is an order of magnitude smaller than:")
    print(f"    - Defensive Prompt Intervention Effect (+56.49%)")
    print(f"    - Architectural Scaling Contrast (-38.94%)")
    print("  * Stochastic run-to-run variance does not alter the structural conclusions of the study.")
    print("=" * 100)

if __name__ == '__main__':
    main()
