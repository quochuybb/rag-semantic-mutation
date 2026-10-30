import os
import hashlib

# Cryptographic SHA-256 Checksums for Experimental and Validation Datasets
# Documented in MANIFEST.md
EXPECTED_HASHES = {
    # 1. Primary Corpus Specifications
    "data/raw/test_cases.csv": "7d7cdc28efc849ce1ff681bbb2042b4de96fd03806121c5de5a6f856bbd52ebc",
    "data_private/private_baseline_dataset.csv": "1de32370d11deffb8a0da59ca8b32418ae64a20fce37aacd4920985a7b8fad21",
    
    # 2. Main Experimental AI Judgements (2,080 Runs across 5 Configurations)
    "llama-3.1-8b-prompt/results/ai_judgements_new.csv": "d5b9c5616d8b16001ac1c5d62902d40cddbab562eb2fb09c2d15193dc840682f",
    "llama-3.1-8b-noprompt/results/ai_judgements_new.csv": "87f95d993d87e751bd8c1910aec7868db23735462ef6909df1cc176748065194",
    "llama-3.1-17b-prompt/results/ai_judgements.csv": "080ea9de34e85abb2e33e6bca554ee476c246fd81b26cca669eaa8bccd8d7054",
    "llama-3.1-17b-noprompt/results/ai_judgements_new.csv": "65a92b4b6a3aed7e721443ff9086e5c3429cca7e23ea17e0a4b13784cc36a669",
    "data_private/results/ai_judge_llama4.csv": "da736e01e83ae13cd2fbbd02adc175c1abbf7deb41183e1231e8c6bc641fc700",
    
    # 3. Clean Baseline Control (Table 5 Paired Comparison)
    "baseline/results/8b_prompt_judged.csv": "cc1950198bf97b282f6c0dc8fc7f48f2c08a66af016e6b72c1f0a9a161a87efe",
    "baseline/results/8b_noprompt_judged.csv": "1921645aad58ab40376a208dba8622aa7b677ba7fd0d96e54e561b1b73e35602",
    "baseline/results/17b_prompt_judged.csv": "73b419dd9e625765335f71721bacaa94edfa6c87a9da410df6f9298955dc6606",
    "baseline/results/17b_noprompt_judged.csv": "79dd8117992fcbe61d091df659c432effad2bbcc80790bc073cc8adf81447edc",
    "baseline/results/17b_prompt_private_judged.csv": "7c74938c5498bba7fca0ad3fd607907280d89fb44d4da2be2d763f8a9df541f5",
    
    # 4. Human Validation Samples (N = 210, 42 per config)
    "llama-3.1-8b-prompt/results/human_eval_sample_new.csv": "1e6483a816a546a834f536dd8163c5b939ef89998345d40a5a5df1fa627a8a47",
    "llama-3.1-8b-noprompt/results/human_eval_sample_new.csv": "141f8c3fb8c6e215f7b433e6c0cba705ff2b86b26583c26cdff1f3383a0a543f",
    "llama-3.1-17b-prompt/results/human_eval_sample_new.csv": "9eddd7c1d92c66cdaebbc8e34668c46fd7572da2f22f8c621a2608f417104c4c",
    "llama-3.1-17b-noprompt/results/human_eval_sample_new.csv": "e4ca1dbf953929b1c64fa095ef1ec8377e3c2eedafcceb9f0ba854655fae95d4",
    "data_private/results/human_eval_sample_new.csv": "698a69198717b206fedb3e0eacb56f7550ec62a2394f3db237e053f0010f42ca",

    # 5. Construct Validity H7: Three-Way Triangulation Audit (N = 52)
    "data/validation/triangulation_h7/h7_stratified_sample_52.csv": "8ddac0bf314b286069501adc53159050e448470cade4f1777d337d08a67172f5",
    "data/validation/triangulation_h7/human_scores_h7.csv": "5f85683e7e987c5d0d72481b3f3b36a87b99ba008133f7f753ebc17dd872431e",
    "data/validation/triangulation_h7/h7_70b_audited_52.csv": "416a11249d454847091592ef26b9294f3cab780aaf9aa2815e46f1224b51c29f",
    "data/validation/triangulation_h7/h7_qwen_audited_52.csv": "ab3e9ad37f37daee8a5c22dc41d19ab2881f76f78e575b763b16c8cd72160db6",
    "data/validation/triangulation_h7/triangulation_3way_52.csv": "675fca082087232d894ee4e5f9c0d555dec50c8bdd5d6141cb07d3db3f002dfe",
    "data/validation/triangulation_h7/h7_mutation_metrics.json": "448765e34cecfab15e0c63096e5e47d8978ae1becd9e2bb76418b328f2db90a9",

    # 6. Internal Validity H4: Run-to-Run Decoding Variance Audit (N = 312)
    "data/validation/variance_h4/h4_sample_104.csv": "26471c3355d8f23d29ab8c7e6a8522aa26a3b067f370690f5d260430b2a7d1c5",
    "data/validation/variance_h4/h4_raw_responses.csv": "57aa6bd9925aa46af0bb034b7191fca66bddc99cbdd9795513a8f8834ce44adc",
    "data/validation/variance_h4/h4_judged_responses.csv": "e15e1b6a5282fce4e7c65e2d1b93433c2c3a928de2bdc8373d5e2eb5a20bc6b1",
    "data/validation/variance_h4/h4_metrics.json": "83641e35453c58fc4c5d49918eabfd5d9a5fbd08cd9464e7d4d1b6d32f9e11b3",

    # 7. Construct Validity H8: Prompt Exemplar Sensitivity (Zero-Shot vs Few-Shot)
    "data/validation/zeroshot_h8/h8_validation_samples_210.csv": "d1a4ff0b830070c17af4eb264d11b6fab39b24b7d6555c57d2d7a1464414efac",
    "data/validation/zeroshot_h8/h8_zeroshot_judged_210.csv": "cf58fe179e82ad6f042d030c8b3edb4d9218a88bea6fd619e6c381e2ae67ed3e",
    "data/validation/zeroshot_h8/h8_sensitivity_metrics.json": "f71d919f16fe6eb16dac6a1ae2844350651e000ea1fd3578520317501e81905d",
}

def verify():
    print("=" * 90)
    print("CRYPTOGRAPHIC INTEGRITY VERIFICATION (SHA-256) ACROSS ALL 30 RESEARCH ARTIFACTS")
    print("=" * 90)
    all_ok = True
    for rel_path, expected in EXPECTED_HASHES.items():
        if not os.path.exists(rel_path):
            print(f"❌ MISSING: {rel_path}")
            all_ok = False
            continue
        with open(rel_path, "rb") as f:
            actual = hashlib.sha256(f.read()).hexdigest()
        if actual.lower() == expected.lower():
            print(f"✅ PASS: {rel_path}")
        else:
            print(f"❌ MISMATCH: {rel_path}")
            print(f"   Expected: {expected}")
            print(f"   Actual:   {actual}")
            all_ok = False
    print("=" * 90)
    if all_ok:
        print(f"🎉 ALL {len(EXPECTED_HASHES)} DATA ARTIFACTS VERIFIED SUCCESSFULLY (100% INTEGRITY).")
    else:
        print("⚠️ SOME ARTIFACTS FAILED VERIFICATION.")
    print("=" * 90)

if __name__ == "__main__":
    verify()
