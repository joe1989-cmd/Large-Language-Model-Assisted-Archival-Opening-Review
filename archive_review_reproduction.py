# Minimal reproduction notes for the paper experiment
# Original experiment was run with Qwen2.5-7B-Instruct, 8-bit quantization.
# Full prompt, archive text, and output are documented in the paper materials.
# This file records the key generation settings used in the reported run.

MODEL = "Qwen2.5-7B-Instruct"
QUANTIZATION = "8-bit"
SEED = 42
MAX_NEW_TOKENS = 1800
DO_SAMPLE = False
REPETITION_PENALTY = 1.03

# Environment observed in the original notebook:
# PyTorch 2.8.0+cu128
# NVIDIA GeForce RTX 4090
# CUDA 12.8
#
# The reported run used:
# - 48 numbered archive paragraphs
# - 15 selected legal-rule entries
# - 5399 input tokens
#
# See:
# archive_review_record_20260922_211712.json
# rule_package_20260922_211712.json
# archive_review_raw_20260922_211712.txt
