# Archive Open Review with Qwen2.5-7B-Instruct

本仓库提供论文实验的最小复现材料，供审稿人查看和下载。

## Files

- `archive_review_reproduction.py`：实验代码，由原始 Jupyter Notebook 导出并保留主要实验流程。
- `rule_package_20260922_211712.json`：本次实验实际调用的档案开放审核规则包。
- `archive_review_record_20260922_211712.json`：完整运行记录，包含案例信息、模型配置、生成参数、System Prompt、User Prompt、档案正文、规则编号及模型输出。
- `archive_review_raw_20260922_211712.txt`：模型原始输出。

## Experiment

Model: Qwen2.5-7B-Instruct  
Quantization: 8-bit  
Seed: 42  
Generation: deterministic (`do_sample=False`)  
Recorded input tokens: 5399

本实验用于验证大语言模型在档案开放审核辅助场景中，对“事实识别—规范适用—风险衡量—处理建议”理由链的生成与留痕能力。模型仅提供辅助意见，不替代档案工作人员的最终审核决定。

## Reproducibility

完整实验输入与输出已经保存在 `archive_review_record_20260922_211712.json` 中。审稿人如仅需核验实验过程，可直接下载该文件和规则包；如需复现实验，可参考 `archive_review_reproduction.py`，并将其中的模型及输入文件路径修改为本地实际路径。

## Notes

论文中的实验结果以本仓库所保存的 2026-09-22 运行记录为准。历史密级和解密状态在案例输入中明确记录为“未提供”，因此模型输出保留了人工核验事项。
