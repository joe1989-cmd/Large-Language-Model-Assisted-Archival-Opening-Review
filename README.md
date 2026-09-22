# LLM-Assisted Archive Open Review: Reproducibility Materials

本仓库保存论文实验的必要过程数据，主要用于同行评审期间核验和下载。

## Included files

- `archive_review_reproduction.py`：记录本次实验的模型、量化方式、随机种子及主要生成参数。
- `archive_review_record_20260922_211712.json`：本次运行的结构化记录，包括案例基本信息、模型配置、输入规模、实际调用规则、引用校验及合规性检查结果。
- `rule_package_20260922_211712.json`：本次实验使用的档案开放审核规则包。
- `archive_review_raw_20260922_211712.txt`：模型未经人工改写的原始输出。

## Experiment configuration

- Model: Qwen2.5-7B-Instruct
- Quantization: 8-bit
- Seed: 42
- max_new_tokens: 1800
- do_sample: false
- repetition_penalty: 1.03
- Recorded input tokens: 5399
- Archive paragraphs: 48
- Rules supplied to the model: 15

原始实验环境记录为 PyTorch 2.8.0+cu128、CUDA 12.8、NVIDIA GeForce RTX 4090。

## Purpose

实验用于考察大语言模型在档案开放审核辅助场景中，对“事实识别—规范适用—风险衡量—处理建议”理由链的生成与留痕能力。

模型输出仅作为辅助审核意见，不替代档案工作人员依法作出的最终审核决定。

## Reviewer access

审稿人可以直接下载本仓库中的 JSON、TXT 和 PY 文件核验实验参数、规则输入、自动校验结果和模型原始输出，无需安装额外项目框架。

论文中引用的本次实验运行时间为：2026-09-22 21:17:12。
