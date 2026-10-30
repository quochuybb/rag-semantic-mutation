# Evaluating RAG Under Adversarial Data at Scale: The Inverse Scaling Law of Semantic Poisoning and the Dynamics of LLM-as-a-Judge

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Replication: Verified](https://img.shields.io/badge/Artifact-100%25%20Verified-brightgreen.svg)](scripts/verify_checksums.py)

Official replication package and artifact repository for the research paper:  
**"Evaluating RAG Under Adversarial Data at Scale: The Inverse Scaling Law of Semantic Poisoning and the Dynamics of LLM-as-a-Judge"**  
*Nguyen Quoc Huy, Le Thi Quynh Chi (FPT University)*  
Target Conference: **ICIIT 2027**

---

## 📌 Abstract & Research Overview

Retrieval-Augmented Generation (RAG) systems mitigate hallucinations by grounding responses in external documents, yet their resilience against subtle, corrupted context remains poorly understood. This repository contains the complete experimental artifacts from a controlled empirical evaluation across **832 AI-generated semantic mutations** (416 public FastAPI and 416 confidential internal enterprise segments) over **2,080 execution runs**.

### Key Findings
1. **Inverse Scaling Law of Semantic Poisoning (RQ1):** Absent a defensive prompt, parameter scale increases compliance with corrupted context: the 17B Mixture-of-Experts (MoE) model abstained in only **3.61%** of cases compared to **42.55%** for the dense 8B model ($h = 1.039, p < 0.001$).
2. **Prompt-Induced Behavioral Convergence (RQ1):** Introducing a defensive system prompt eliminates cross-architecture divergence, compressing abstention rates into a shared ceiling ($\approx 60\%$--$64\%, p = 0.284$).
3. **Vulnerability on Private Enterprise Data (RQ2):** On confidential documentation lacking pre-training exposure, parametric correction drops from **9.37%** to **2.88%** ($p < 0.001$), while context compliance escalates to **45.19%** ($p < 0.001$).
4. **LLM-as-a-Judge Validation:** Automated scoring by Llama 4 Scout 17B achieved substantial-to-almost-perfect agreement with an independent human evaluator ($N = 210, 90.95\%$ agreement, Cohen's $\kappa = 0.858$).

---

## 📂 Repository Structure

```text
rag-semantic-mutation/
├── README.md               # This documentation
├── MANIFEST.md             # Complete inventory, checksums, system & model specs
├── requirements.txt        # Python library dependencies
├── .gitignore              # Git ignore rules
│
├── data/                   # Public corpus, mutations & validation sets
│   ├── raw/
│   │   └── test_cases.csv  # 416 mutation test cases (SHA-256 verified)
│   ├── baseline_docs/      # 32 clean reference markdown documents
│   ├── mutated_md_files/   # 416 mutated markdown documents across 13 operators
│   └── validation/         # Empirical validation & audit artifacts
│       ├── triangulation_h7/  # H7 3-way triangulation (Human vs 70B vs 72B, N=52)
│       ├── variance_h4/       # H4 Run variance repeated generations (N=312)
│       └── zeroshot_h8/       # H8 Zero-shot vs 5-shot sensitivity (N=210)
│
├── data_private/           # Private enterprise corpus & mutations
│   ├── private_baseline_dataset.csv # 32 baseline reference documents
│   ├── private_mutated_dataset.csv  # 416 SMART mutated documents
│   ├── docs/               # 32 source markdown files
│   ├── mutated_md_files/   # 416 mutated markdown files
│   └── results/            # 17B Private evaluation outputs
│       ├── ai_judge_llama4.csv
│       ├── full_mutated_responses.csv
│       ├── baseline_responses.csv
│       └── human_eval_sample_new.csv
│
├── llama-3.1-8b-prompt/    # Arm 1: 8B With Defensive Prompt (Public)
│   └── results/
│       ├── ai_judgements_new.csv
│       ├── full_mutated_responses.csv
│       ├── baseline_responses.csv
│       └── human_eval_sample_new.csv
│
├── llama-3.1-8b-noprompt/  # Arm 1: 8B Without Defensive Prompt (Public)
│   └── results/
│       ├── ai_judgements_new.csv
│       ├── full_mutated_responses.csv
│       ├── baseline_responses.csv
│       └── human_eval_sample_new.csv
│
├── llama-3.1-17b-prompt/   # Arm 2: 17B MoE With Defensive Prompt (Public)
│   └── results/
│       ├── ai_judgements.csv
│       ├── full_mutated_responses.csv
│       ├── baseline_responses.csv
│       └── human_eval_sample_new.csv
│
├── llama-3.1-17b-noprompt/ # Arm 2: 17B MoE Without Defensive Prompt (Public)
│   └── results/
│       ├── ai_judgements_new.csv
│       ├── full_mutated_responses.csv
│       ├── baseline_responses.csv
│       └── human_eval_sample_new.csv
│
├── baseline/               # Paired clean-control baselines and statistical scripts
│   ├── compute_paired_comparison.py
│   └── results/
│       ├── 8b_prompt_judged.csv
│       ├── 8b_noprompt_judged.csv
│       ├── 17b_prompt_judged.csv
│       ├── 17b_noprompt_judged.csv
│       ├── 17b_prompt_private_judged.csv
│       ├── paired_comparison_summary.csv
│       └── paired_table.tex
│
├── scripts/                # Execution & analysis scripts
│   ├── reproduce_all_tables.py             # 1-Click Master Reproduction Suite
│   ├── verify_checksums.py                 # 1-Click SHA-256 integrity check (30 files)
│   ├── compute_table4_overall_results.py   # Table 4 (Kappa & distributions across 5 configs)
│   ├── compute_table6_confirmatory_contrasts.py # Table 6 (Cluster-robust & Holm p-values)
│   ├── compute_table7_sensitivity_benchmarks.py # Table 7 (Exact binomial tests vs 50/75/90%)
│   ├── compute_table8_confusion_matrix.py  # Table 8 (Human vs AI Judge confusion matrix)
│   ├── compute_h7_triangulation.py         # Section 6.1 (Construct Validity Triangulation)
│   ├── compute_h4_run_variance.py          # Section 6.2 (Internal Validity Run Variance)
│   ├── compute_h8_zeroshot_sensitivity.py  # Section 5.3 (Zero-shot Exemplar Sensitivity)
│   ├── compute_paired_comparison.py        # Table 5 Paired clean vs mutated script
│   ├── global_setup_workspaces.py          # Workspace initialization
│   ├── global_run_batched_attack_prompt.py
│   ├── global_run_batched_attack_noprompt.py
│   ├── global_run_baseline_full_prompt.py
│   ├── global_run_baseline_full_noprompt.py
│   └── data_private_run_private_ai_judge_llama4.py
│
└── prompts/                # Verbatim prompt templates & judge rubrics
    ├── defensive_system_prompt.txt
    ├── mutation_prompt_public.txt
    ├── mutation_prompt_private_smart.txt
    └── llm_judge_rubric.txt
```

---

## 🚀 Quick Start & Replication

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/quochuybb/rag-semantic-mutation.git
cd rag-semantic-mutation

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Cryptographic Data Integrity
To verify that all 30 evaluation CSV files and datasets are authentic and untampered:
```bash
python scripts/verify_checksums.py
```
*Expected output: `ALL 30 DATA ARTIFACTS VERIFIED SUCCESSFULLY (100% INTEGRITY)`.*

### 3. Master 1-Click Reproduction of All Paper Tables & Validity Audits
To reproduce all tables and empirical statistics in `main.tex` and `main_iciit.tex`:
```bash
python scripts/reproduce_all_tables.py
```
This executes and verifies:
1. **Table 4 (`tab:results`):** 5-configuration behavior distribution and inter-annotator agreement ($N=210, 90.95\%$ agreement, $\kappa = 0.858$, 95% CI: $[0.797, 0.919]$).
2. **Table 5 (`tab:paired_clean_mutated`):** Paired differences between clean controls ($N=32$) and mutated runs ($N=416$) with cluster-robust standard errors ($df = 31$).
3. **Table 6 (`tab:confirmatory_contrasts` / `tab:stat_summary`):** Confirmatory contrasts under independent Wald and Cluster-Robust models with Holm-Bonferroni FWER control.
4. **Table 7 (`tab:sensitivity_benchmarks` / `tab:binom_summary`):** Exact binomial sensitivity tests against $50\%, 75\%, 90\%, 95\%$ operational benchmarks.
5. **Table 8 (`tab:judge_confusion`):** Complete 4x4 confusion matrix between Human Evaluator and AI Judge ($91, 6, 65, 6, 35, 1$).
6. **Construct Validity Audit (H7):** Three-way triangulation ($N=52$) with Human, Llama-3.3-70B, and Qwen-2.5-72B ($80.77\%$ consensus, Human-70B $\kappa=0.705$, Fleiss $\kappa=0.444$).
7. **Internal Validity Audit (H4):** Run-to-run decoding variance across 312 runs at $\text{temp}=0.7$ ($\text{SD} = \pm 6.40\%$, label-switch rate $39.42\%$).
8. **Exemplar Sensitivity Audit (H8):** Zero-Shot vs. 5-Shot Judge agreement comparison ($N=210, \kappa = 0.849$ vs. $0.858$, $\Delta \kappa = +0.009$).

---

## 📊 Summary of Experimental Arms

| Config | Model Architecture | Parameters | Prompt Treatment | Dataset Domain | Mutated Runs ($N$) | Clean Baseline ($N$) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| **Config 1** | Llama 4 Scout 17B-16E | 17B Active MoE | With Defensive Prompt | Public (FastAPI) | 416 | 32 |
| **Config 2** | Llama 4 Scout 17B-16E | 17B Active MoE | Without Prompt | Public (FastAPI) | 416 | 32 |
| **Config 3** | Llama 3.1 8B Instruct | 8.03B Dense | With Defensive Prompt | Public (FastAPI) | 416 | 32 |
| **Config 4** | Llama 3.1 8B Instruct | 8.03B Dense | Without Prompt | Public (FastAPI) | 416 | 32 |
| **Config 5** | Llama 4 Scout 17B-16E | 17B Active MoE | With Defensive Prompt | Private (Internal) | 416 | 32 |
| **Total** | | | | | **2,080 runs** | **160 runs** |

---

## 📜 Citation

If you find this replication package, dataset, or benchmark methodology helpful in your research, please cite our paper:

```bibtex
@inproceedings{nguyen2027evaluating,
  title={Evaluating RAG Under Adversarial Data at Scale: The Inverse Scaling Law of Semantic Poisoning and the Dynamics of LLM-as-a-Judge},
  author={Nguyen, Quoc Huy and Le, Thi Quynh Chi},
  booktitle={Proceedings of the 12th International Conference on Intelligent Information Technology (ICIIT 2027)},
  year={2027},
  publisher={ACM},
  doi={https://doi.org/10.1145/xxxxxxx.xxxxxxx}
}
```

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE).