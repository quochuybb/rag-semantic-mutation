import os
import csv
import re
import math
import numpy as np
from scipy import stats

def get_cluster(mut_id):
    m = re.match(r"^(CTX_\d{3}|sjs_\d{3})", mut_id)
    return m.group(1) if m else mut_id

LABELS = ["Faithful", "Abstain", "Inconsistent", "Hallucination"]

CONFIGS = [
    {
        "id": "Config 1",
        "name": "Llama 3.1 8B Without Prompt (Public)",
        "clean_file": "baseline/results/8b_noprompt_judged.csv",
        "mut_file": "llama-3.1-8b-noprompt/results/ai_judgements_new.csv"
    },
    {
        "id": "Config 2",
        "name": "Llama 3.1 8B With Prompt (Public)",
        "clean_file": "baseline/results/8b_prompt_judged.csv",
        "mut_file": "llama-3.1-8b-prompt/results/ai_judgements_new.csv"
    },
    {
        "id": "Config 3",
        "name": "Llama 4 Scout Without Prompt (Public)",
        "clean_file": "baseline/results/17b_noprompt_judged.csv",
        "mut_file": "llama-3.1-17b-noprompt/results/ai_judgements_new.csv"
    },
    {
        "id": "Config 4",
        "name": "Llama 4 Scout With Prompt (Public)",
        "clean_file": "baseline/results/17b_prompt_judged.csv",
        "mut_file": "llama-3.1-17b-prompt/results/ai_judgements.csv"
    },
    {
        "id": "Config 5",
        "name": "Llama 4 Scout With Prompt (Private)",
        "clean_file": "baseline/results/17b_prompt_private_judged.csv",
        "mut_file": "data_private/results/ai_judge_llama4.csv"
    }
]

def analyze_config(cfg):
    # 1. Load Clean Baseline
    clean_map = {}
    with open(cfg["clean_file"], "r", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r.get("ai_label") not in ["Error", ""]:
                clean_map[r["id"]] = r["ai_label"]

    # 2. Load Mutated
    mut_clusters = {}
    with open(cfg["mut_file"], "r", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            cid = get_cluster(r["mut_id"])
            if cid not in mut_clusters:
                mut_clusters[cid] = []
            mut_clusters[cid].append(r["ai_label"])

    clusters = sorted(clean_map.keys())
    K = len(clusters) # 32 clusters

    results = []

    for label in LABELS:
        clean_rates = []
        mut_rates = []
        paired_diffs = []

        for cid in clusters:
            # Clean indicator: 1 if match label, else 0
            c_val = 1.0 if clean_map[cid] == label else 0.0
            clean_rates.append(c_val)

            # Mutated rate for this cluster
            m_list = mut_clusters[cid]
            m_val = sum(1.0 for x in m_list if x == label) / len(m_list)
            mut_rates.append(m_val)

            # Paired difference (Mutated - Clean)
            paired_diffs.append(m_val - c_val)

        clean_rates = np.array(clean_rates)
        mut_rates = np.array(mut_rates)
        diffs = np.array(paired_diffs)

        mean_clean = np.mean(clean_rates) * 100.0
        mean_mut = np.mean(mut_rates) * 100.0
        mean_diff = np.mean(diffs) * 100.0 # Delta in percentage points

        # Cluster-robust standard error
        # SE = s_d / sqrt(K)
        std_diff = np.std(diffs, ddof=1) * 100.0
        se_cluster = std_diff / math.sqrt(K)

        # 95% Confidence Interval using t-distribution (df = K - 1 = 31)
        df = K - 1
        t_crit = stats.t.ppf(0.975, df)
        ci_lower = mean_diff - t_crit * se_cluster
        ci_upper = mean_diff + t_crit * se_cluster

        # Paired t-test
        t_stat = mean_diff / se_cluster if se_cluster > 0 else 0.0
        p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df)) if se_cluster > 0 else 1.0

        # Cluster Bootstrap 95% CI (2,000 resamples)
        np.random.seed(42)
        boot_diffs = []
        for _ in range(2000):
            idx = np.random.choice(K, size=K, replace=True)
            boot_diffs.append(np.mean(diffs[idx]) * 100.0)
        boot_ci_lower = np.percentile(boot_diffs, 2.5)
        boot_ci_upper = np.percentile(boot_diffs, 97.5)

        results.append({
            "label": label,
            "mean_clean": mean_clean,
            "mean_mut": mean_mut,
            "delta": mean_diff,
            "se_cluster": se_cluster,
            "ci_lower": ci_lower,
            "ci_upper": ci_upper,
            "boot_ci_lower": boot_ci_lower,
            "boot_ci_upper": boot_ci_upper,
            "p_val": p_val
        })

    return results

def main():
    print("=" * 115)
    print("🔬 BẢNG SO SÁNH GHÉP CẶP CLEAN VS. MUTATED VÀ 95% CLUSTER CONFIDENCE INTERVALS (K = 32 CLUSTERS) 🔬")
    print("=" * 115)

    all_data = []

    for cfg in CONFIGS:
        print(f"\n📌 {cfg['name']} (N_clean = 32, N_mutated = 416)")
        print(f"{'Label':<15} | {'Clean (%)':<10} | {'Mutated (%)':<12} | {'Delta (pp)':<11} | {'Cluster SE':<11} | {'Cluster 95% CI':<24} | {'p-value':<9}")
        print("-" * 115)
        
        cfg_res = analyze_config(cfg)
        for r in cfg_res:
            p_str = "< 0.001" if r["p_val"] < 0.001 else f"{r['p_val']:.4f}"
            ci_str = f"[{r['ci_lower']:+6.2f}, {r['ci_upper']:+6.2f}]"
            print(f"{r['label']:<15} | {r['mean_clean']:>8.2f}% | {r['mean_mut']:>10.2f}% | {r['delta']:>+9.2f}% | {r['se_cluster']:>9.2f}% | {ci_str:<24} | {p_str:<9}")
            all_data.append({
                "config_id": cfg["id"],
                "config_name": cfg["name"],
                "label": r["label"],
                "clean_pct": f"{r['mean_clean']:.2f}",
                "mutated_pct": f"{r['mean_mut']:.2f}",
                "delta_pp": f"{r['delta']:.2f}",
                "cluster_se": f"{r['se_cluster']:.2f}",
                "ci_lower": f"{r['ci_lower']:.2f}",
                "ci_upper": f"{r['ci_upper']:.2f}",
                "boot_ci_lower": f"{r['boot_ci_lower']:.2f}",
                "boot_ci_upper": f"{r['boot_ci_upper']:.2f}",
                "p_val": f"{r['p_val']:.5f}"
            })

    # Save to CSV
    os.makedirs("baseline/results", exist_ok=True)
    out_csv = "baseline/results/paired_comparison_summary.csv"
    with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
        fieldnames = list(all_data[0].keys())
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_data)

    print("\n" + "=" * 115)
    print(f"✅ Đã lưu kết quả chi tiết dạng CSV tại: {out_csv}")

    # Generate LaTeX Table for main.tex
    tex_path = "baseline/results/paired_table.tex"
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write("% ==============================================================================\n")
        f.write("% PAIRED CLEAN-VERSUS-MUTATED EVALUATION TABLE (RESOLVING BLOCKING 1 / R1)\n")
        f.write("% ==============================================================================\n")
        f.write("\\begin{table*}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\small\n")
        f.write("\\caption{Paired Clean-versus-Mutated Comparison across 32 Source Segments (Clusters) with Cluster-Robust 95\\% Confidence Intervals ($K=32$ clusters, $N_{\\text{clean}}=32$, $N_{\\text{mutated}}=416$).}\n")
        f.write("\\label{tab:paired_clean_mutated}\n")
        f.write("\\begin{tabular}{llccccc}\n")
        f.write("\\toprule\n")
        f.write("\\textbf{Configuration} & \\textbf{Label} & \\textbf{Clean (\\%)} & \\textbf{Mutated (\\%)} & \\textbf{Paired $\\Delta$ (pp)} & \\textbf{Cluster 95\\% CI} & \\textbf{$p$-value} \\\\\n")
        f.write("\\midrule\n")

        for cfg in CONFIGS:
            cfg_rows = [x for x in all_data if x["config_name"] == cfg["name"]]
            short_cfg_name = cfg["name"]
            for i, r in enumerate(cfg_rows):
                prefix = f"\\multirow{{4}}{{*}}{{{short_cfg_name}}}" if i == 0 else ""
                delta_sign = "+" if float(r["delta_pp"]) > 0 else ""
                p_disp = "< 0.001" if float(r["p_val"]) < 0.001 else f"{float(r['p_val']):.3f}"
                if float(r["p_val"]) < 0.05:
                    p_disp += "$^{*}$"
                if float(r["p_val"]) < 0.001:
                    p_disp += "$^{*}$"
                ci_str = f"[{r['ci_lower']}, {r['ci_upper']}]"
                f.write(f"{prefix} & {r['label']} & {r['clean_pct']}\\% & {r['mutated_pct']}\\% & {delta_sign}{r['delta_pp']} pp & {ci_str} & {p_disp} \\\\\n")
            f.write("\\midrule\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\begin{tablenotes}\n")
        f.write("\\footnotesize\n")
        f.write("\\item \\textit{Note:} Paired $\\Delta = P(\\text{Mutated}) - P(\\text{Clean})$ at the source segment level. Standard errors and 95\\% confidence intervals are clustered at the source segment level ($K=32$ clusters, degrees of freedom $df=31$). Statistical significance: $^{*}p < 0.05$, $^{**}p < 0.001$.\n")
        f.write("\\end{tablenotes}\n")
        f.write("\\end{table*}\n")

    print(f"✅ Đã sinh mã bảng LaTeX hoàn chỉnh tại: {tex_path}")

if __name__ == "__main__":
    main()
