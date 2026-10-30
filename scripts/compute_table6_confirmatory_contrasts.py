"""
Reproduce Table 6 (Confirmatory Pairwise Comparisons Evaluated Under Independent
and Cluster-Robust Models).

Paper Reference:
- main_iciit.tex: Table 6 (tab:confirmatory_contrasts) & Section 4.2
- main.tex: Table 11 (tab:stat_summary) & Section 4.7
"""

import os
import sys
import csv
import math
import numpy as np
from scipy import stats

def load_data(filepath):
    data = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mut_id = row['mut_id'].strip()
            label = row['ai_label'].strip()
            if '_MUT_' in mut_id:
                parts = mut_id.split('_MUT_')
                cluster = parts[0]
                op = int(parts[1])
            else:
                cluster = mut_id
                op = 0
            data.append({
                'mut_id': mut_id,
                'cluster': cluster,
                'op': op,
                'label': label
            })
    return data

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    files = {
        '17B_prompt': os.path.join(repo_root, 'llama-3.1-17b-prompt', 'results', 'ai_judgements.csv'),
        '17B_noprompt': os.path.join(repo_root, 'llama-3.1-17b-noprompt', 'results', 'ai_judgements_new.csv'),
        '8B_prompt': os.path.join(repo_root, 'llama-3.1-8b-prompt', 'results', 'ai_judgements_new.csv'),
        '8B_noprompt': os.path.join(repo_root, 'llama-3.1-8b-noprompt', 'results', 'ai_judgements_new.csv'),
        'private_prompt': os.path.join(repo_root, 'data_private', 'results', 'ai_judge_llama4.csv')
    }
    
    datasets = {k: load_data(v) for k, v in files.items()}

    comparisons = [
        {
            'name': 'Prompt Effect (17B)',
            'metric': 'Abstain',
            'type': 'paired',
            'dataA': datasets['17B_prompt'],
            'dataB': datasets['17B_noprompt'],
        },
        {
            'name': 'Prompt Effect (8B)',
            'metric': 'Abstain',
            'type': 'paired',
            'dataA': datasets['8B_prompt'],
            'dataB': datasets['8B_noprompt'],
        },
        {
            'name': 'Model Scale (Prompted)',
            'metric': 'Abstain',
            'type': 'paired',
            'dataA': datasets['17B_prompt'],
            'dataB': datasets['8B_prompt'],
        },
        {
            'name': 'Model Scale (Unprompted)',
            'metric': 'Abstain',
            'type': 'paired',
            'dataA': datasets['17B_noprompt'],
            'dataB': datasets['8B_noprompt'],
        },
        {
            'name': 'Data Domain (17B Prompt)',
            'metric': 'Inconsistent',
            'type': 'two_sample',
            'dataA': datasets['17B_prompt'],
            'dataB': datasets['private_prompt'],
        },
        {
            'name': 'Data Domain (17B Prompt)',
            'metric': 'Faithful',
            'type': 'two_sample',
            'dataA': datasets['17B_prompt'],
            'dataB': datasets['private_prompt'],
        }
    ]

    print("=" * 135)
    print("TABLE 6: CONFIRMATORY PAIRWISE COMPARISONS EVALUATED UNDER INDEPENDENT AND CLUSTER-ROBUST MODELS")
    print("=" * 135)

    results = []
    np.random.seed(42)
    B_BOOT = 10000

    for comp in comparisons:
        target_metric = comp['metric']
        dataA = comp['dataA']
        dataB = comp['dataB']
        
        # 1. Unadjusted Wald Z-test
        nA = len(dataA)
        nB = len(dataB)
        countA = sum(1 for d in dataA if d['label'] == target_metric)
        countB = sum(1 for d in dataB if d['label'] == target_metric)
        pA = countA / nA
        pB = countB / nB
        diff_wald = pA - pB
        se_wald = math.sqrt(pA * (1 - pA) / nA + pB * (1 - pB) / nB)
        ci_wald_low = diff_wald - 1.96 * se_wald
        ci_wald_high = diff_wald + 1.96 * se_wald

        # 2. Cluster Analysis
        if comp['type'] == 'paired':
            clustersA = {}
            clustersB = {}
            for d in dataA:
                clustersA.setdefault(d['cluster'], []).append(1 if d['label'] == target_metric else 0)
            for d in dataB:
                clustersB.setdefault(d['cluster'], []).append(1 if d['label'] == target_metric else 0)
            
            cluster_names = sorted(list(clustersA.keys()))
            K = len(cluster_names)
            ratesA = np.array([np.mean(clustersA[c]) for c in cluster_names])
            ratesB = np.array([np.mean(clustersB[c]) for c in cluster_names])
            d_k = ratesA - ratesB
            
            mean_d = np.mean(d_k)
            sd_d = np.std(d_k, ddof=1)
            se_cluster = sd_d / math.sqrt(K)
            df = K - 1
            t_crit = stats.t.ppf(0.975, df)
            ci_cluster_low = mean_d - t_crit * se_cluster
            ci_cluster_high = mean_d + t_crit * se_cluster
            t_stat = mean_d / se_cluster if se_cluster > 0 else 0
            p_cluster = 2 * (1 - stats.t.cdf(abs(t_stat), df))

            # Cluster Bootstrap
            boot_diffs = []
            for _ in range(B_BOOT):
                boot_idx = np.random.choice(K, size=K, replace=True)
                boot_diffs.append(np.mean(d_k[boot_idx]))
            ci_boot_low, ci_boot_high = np.percentile(boot_diffs, [2.5, 97.5])

        else: # two_sample
            clustersA = {}
            clustersB = {}
            for d in dataA:
                clustersA.setdefault(d['cluster'], []).append(1 if d['label'] == target_metric else 0)
            for d in dataB:
                clustersB.setdefault(d['cluster'], []).append(1 if d['label'] == target_metric else 0)

            namesA = sorted(list(clustersA.keys()))
            namesB = sorted(list(clustersB.keys()))
            KA, KB = len(namesA), len(namesB)
            ratesA = np.array([np.mean(clustersA[c]) for c in namesA])
            ratesB = np.array([np.mean(clustersB[c]) for c in namesB])
            
            meanA = np.mean(ratesA)
            meanB = np.mean(ratesB)
            mean_d = meanA - meanB
            varA = np.var(ratesA, ddof=1)
            varB = np.var(ratesB, ddof=1)
            se_cluster = math.sqrt(varA / KA + varB / KB)
            df = (varA / KA + varB / KB)**2 / ((varA / KA)**2 / (KA - 1) + (varB / KB)**2 / (KB - 1))
            t_crit = stats.t.ppf(0.975, df)
            ci_cluster_low = mean_d - t_crit * se_cluster
            ci_cluster_high = mean_d + t_crit * se_cluster
            t_stat = mean_d / se_cluster if se_cluster > 0 else 0
            p_cluster = 2 * (1 - stats.t.cdf(abs(t_stat), df))

            # Cluster Bootstrap
            boot_diffs = []
            for _ in range(B_BOOT):
                idxA = np.random.choice(KA, size=KA, replace=True)
                idxB = np.random.choice(KB, size=KB, replace=True)
                boot_diffs.append(np.mean(ratesA[idxA]) - np.mean(ratesB[idxB]))
            ci_boot_low, ci_boot_high = np.percentile(boot_diffs, [2.5, 97.5])

        results.append({
            'name': comp['name'],
            'metric': target_metric,
            'diff': mean_d * 100,
            'ci_wald': (ci_wald_low * 100, ci_wald_high * 100),
            'ci_cluster': (ci_cluster_low * 100, ci_cluster_high * 100),
            'ci_boot': (ci_boot_low * 100, ci_boot_high * 100),
            'p_cluster': p_cluster,
            't_stat': t_stat,
            'df': df
        })

    # Holm-Bonferroni correction on p_cluster
    sorted_indices = sorted(range(len(results)), key=lambda i: results[i]['p_cluster'])
    m = len(results)
    adj_p = [0.0] * m
    cum_max = 0.0
    for rank, idx in enumerate(sorted_indices):
        raw_p = results[idx]['p_cluster']
        pval_corrected = min(1.0, raw_p * (m - rank))
        cum_max = max(cum_max, pval_corrected)
        adj_p[idx] = cum_max

    for i, r in enumerate(results):
        r['holm_p_adj'] = adj_p[i]

    header = f"{'Comparison':<28} | {'Metric':<12} | {'Diff (pp)':<9} | {'Wald 95% CI':<19} | {'Cluster-Robust 95% CI':<24} | {'Raw p_cluster':<14} | {'Holm p_adj':<12}"
    print(header)
    print("-" * 135)
    for r in results:
        w_ci = f"[{r['ci_wald'][0]:+6.2f}, {r['ci_wald'][1]:+6.2f}]"
        c_ci = f"[{r['ci_cluster'][0]:+6.2f}, {r['ci_cluster'][1]:+6.2f}]"
        raw_p_str = f"{r['p_cluster']:.2e}" if r['p_cluster'] < 0.001 else f"{r['p_cluster']:.3f}"
        adj_p_str = f"{r['holm_p_adj']:.2e}" if r['holm_p_adj'] < 0.001 else f"{r['holm_p_adj']:.3f}"
        print(f"{r['name']:<28} | {r['metric']:<12} | {r['diff']:+7.2f}% | {w_ci:<19} | {c_ci:<24} | {raw_p_str:<14} | {adj_p_str:<12}")

    print("=" * 135)

if __name__ == '__main__':
    main()
