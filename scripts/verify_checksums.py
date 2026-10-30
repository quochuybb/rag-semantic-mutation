import os
import hashlib

# Expected SHA-256 hashes from MANIFEST.md
EXPECTED_HASHES = {
    "data/raw/test_cases.csv": "7d7cdc28efc849ce1ff681bbb2042b4de96fd03806121c5de5a6f856bbd52ebc",
    "data_private/private_baseline_dataset.csv": "1de32370d11deffb8a0da59ca8b32418ae64a20fce37aacd4920985a7b8fad21",
    "llama-3.1-8b-prompt/results/ai_judgements_new.csv": "d5b9c5616d8b16001ac1c5d62902d40cddbab562eb2fb09c2d15193dc840682f",
    "llama-3.1-8b-noprompt/results/ai_judgements_new.csv": "87f95d993d87e751bd8c1910aec7868db23735462ef6909df1cc176748065194",
    "llama-3.1-17b-prompt/results/ai_judgements.csv": "080ea9de34e85abb2e33e6bca554ee476c246fd81b26cca669eaa8bccd8d7054",
    "llama-3.1-17b-noprompt/results/ai_judgements_new.csv": "65a92b4b6a3aed7e721443ff9086e5c3429cca7e23ea17e0a4b13784cc36a669",
    "data_private/results/ai_judge_llama4.csv": "da736e01e83ae13cd2fbbd02adc175c1abbf7deb41183e1231e8c6bc641fc700",
    "baseline/results/8b_prompt_judged.csv": "cc1950198bf97b282f6c0dc8fc7f48f2c08a66af016e6b72c1f0a9a161a87efe",
    "baseline/results/8b_noprompt_judged.csv": "1921645aad58ab40376a208dba8622aa7b677ba7fd0d96e54e561b1b73e35602",
    "baseline/results/17b_prompt_judged.csv": "73b419dd9e625765335f71721bacaa94edfa6c87a9da410df6f9298955dc6606",
    "baseline/results/17b_noprompt_judged.csv": "79dd8117992fcbe61d091df659c432effad2bbcc80790bc073cc8adf81447edc",
    "baseline/results/17b_prompt_private_judged.csv": "7c74938c5498bba7fca0ad3fd607907280d89fb44d4da2be2d763f8a9df541f5",
    "llama-3.1-8b-prompt/results/human_eval_sample_new.csv": "1e6483a816a546a834f536dd8163c5b939ef89998345d40a5a5df1fa627a8a47",
    "llama-3.1-8b-noprompt/results/human_eval_sample_new.csv": "141f8c3fb8c6e215f7b433e6c0cba705ff2b86b26583c26cdff1f3383a0a543f",
    "llama-3.1-17b-prompt/results/human_eval_sample_new.csv": "9eddd7c1d92c66cdaebbc8e34668c46fd7572da2f22f8c621a2608f417104c4c",
    "llama-3.1-17b-noprompt/results/human_eval_sample_new.csv": "e4ca1dbf953929b1c64fa095ef1ec8377e3c2eedafcceb9f0ba854655fae95d4",
    "data_private/results/human_eval_sample_new.csv": "698a69198717b206fedb3e0eacb56f7550ec62a2394f3db237e053f0010f42ca",
}

def verify():
    print("=" * 80)
    print("CRYPTOGRAPHIC INTEGRITY VERIFICATION (SHA-256)")
    print("=" * 80)
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
    print("=" * 80)
    if all_ok:
        print("🎉 ALL 17 DATA ARTIFACTS VERIFIED SUCCESSFULLY (100% INTEGRITY).")
    else:
        print("⚠️ SOME ARTIFACTS FAILED VERIFICATION.")
    print("=" * 80)

if __name__ == "__main__":
    verify()
