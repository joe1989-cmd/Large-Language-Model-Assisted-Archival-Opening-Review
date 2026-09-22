# LLM-Assisted Archive Open Review: Reproducibility Materials

本仓库保存论文实验的完整过程数据，主要用于同行评审期间核验、下载和复现实验。

## Included files

### Experiment code and outputs

- `Qwen2.5-archive_review.ipynb`：本次实验实际使用的 Jupyter Notebook，包含模型加载、提示词构造、规则调用、生成与结果记录等主要实验流程。
- `archive_review_reproduction.py`：记录本次实验的模型、量化方式、随机种子及主要生成参数的简化复现说明。
- `archive_review_record_20260922_211712.json`：本次运行的结构化记录，包括案例基本信息、模型配置、生成参数、输入规模、实际调用规则、提示词、档案正文、模型输出及自动校验信息。
- `archive_review_raw_20260922_211712.txt`：模型未经人工改写的原始输出。
- `rule_package_20260922_211712.json`：本次实验实际提供给模型的档案开放审核规则包。

### Source materials

- `北京市人民政府对《市城市规划设计研究院关于金海风景区总体规划请示》的批复.docx`：实验案例原始文件。
- `中华人民共和国档案法.docx`：实验规则来源文件之一。
- `中华人民共和国档案法实施条例.docx`：实验规则来源文件之一。
- `国家档案馆档案开放办法.docx`：实验规则来源文件之一。
- `平谷区馆藏档案开放目录.xlsx`：用于案例筛选与现实开放情况核验的公开档案目录数据。

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

## Reproduction

如需核验论文中的实验结果，可直接查看 `archive_review_record_20260922_211712.json`、`rule_package_20260922_211712.json` 和 `archive_review_raw_20260922_211712.txt`。

如需完整复现实验，可运行 `Qwen2.5-archive_review.ipynb`，并根据本地环境调整模型路径和文件路径。原始案例、规则来源文件及开放目录数据均已保存在本仓库中。

论文中引用的本次实验运行时间为：2026-09-22 21:17:12。
