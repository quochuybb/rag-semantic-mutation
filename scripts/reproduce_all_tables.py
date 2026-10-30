"""
Master Reproduction Script: End-to-End Replication of All Empirical Tables,
Statistical Tests, and Validity Audits in the Research Paper.

Paper: Evaluating RAG Under Adversarial Data at Scale:
       The Inverse Scaling Law of Semantic Poisoning and the Dynamics of LLM-as-a-Judge
Target Venue: ICIIT 2027 (ACM ICPS) / SOICT 2026

Usage:
    python scripts/reproduce_all_tables.py
"""

import os
import sys
import subprocess

def run_step(step_name, script_path):
    print("\n" + "#" * 90)
    print(f"# EXECUTION STEP: {step_name}")
    print(f"# SCRIPT: {script_path}")
    print("#" * 90 + "\n")
    
    python_exe = sys.executable
    result = subprocess.run([python_exe, script_path], capture_output=False, text=True)
    if result.returncode != 0:
        print(f"ERROR: Execution of {script_path} failed with return code {result.returncode}!")
        return False
    return True

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("=" * 90)
    print("MASTER REPLICATION SUITE: REPRODUCING ALL RESULTS FOR MAIN.TEX & MAIN_ICIIT.TEX")
    print("=" * 90)

    steps = [
        ("Table 4: Summary of RAG Evaluation Results & Inter-Annotator Agreement", 
         os.path.join(repo_root, "scripts", "compute_table4_overall_results.py")),
        ("Table 5: Paired Clean-versus-Mutated Comparison across 32 Clusters", 
         os.path.join(repo_root, "baseline", "compute_paired_comparison.py")),
        ("Table 6: Confirmatory Pairwise Contrasts & Cluster-Robust Statistics", 
         os.path.join(repo_root, "scripts", "compute_table6_confirmatory_contrasts.py")),
        ("Table 7: Sensitivity Analysis Across Operational Abstention Benchmarks", 
         os.path.join(repo_root, "scripts", "compute_table7_sensitivity_benchmarks.py")),
        ("Table 8: Confusion Matrix Between Human Evaluator and AI Judge (N=210)", 
         os.path.join(repo_root, "scripts", "compute_table8_confusion_matrix.py")),
        ("Construct Validity (H7): Three-Way Triangulation Audit (N=52)", 
         os.path.join(repo_root, "scripts", "compute_h7_triangulation.py")),
        ("Internal Validity (H4): Run-to-Run Decoding Variance Audit (N=312)", 
         os.path.join(repo_root, "scripts", "compute_h4_run_variance.py")),
        ("Construct Validity (H8): Prompt Exemplar Sensitivity (Zero-Shot vs Few-Shot)", 
         os.path.join(repo_root, "scripts", "compute_h8_zeroshot_sensitivity.py")),
    ]

    all_ok = True
    for name, path in steps:
        if not run_step(name, path):
            all_ok = False
            break

    print("\n" + "=" * 90)
    if all_ok:
        print("SUCCESS: ALL TABLES AND EMPIRICAL ANALYSES REPRODUCED WITH 100% PASS RATE!")
    else:
        print("FAILURE: ONE OR MORE REPLICATION STEPS ENCOUNTERED ERRORS.")
    print("=" * 90)

if __name__ == '__main__':
    main()
