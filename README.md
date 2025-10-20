# MLLM-ISU
The First-Ever Comprehensive Benchmark for Multimodal Large Language Models based Intrusion Scene Understanding
--
Introcution
Vision-based intrusion detection has multiple applications in practical scenarios, e.g., autonomous driving, intelligent monitoring, and security. Previous works
mainly focus on improving the intrusion detection performance, without a comprehensive and in-depth understanding of the intrusion scene. To fill this gap, we
explore a novel task called Multimodal Large Language Models based Intrusion Scene Understanding (MLLM-ISU) and report a comprehensive benchmark for the
task. Specifically, we first design an effective and automatic visual question-answer generation strategy, constructing a new MLLM-ISU dataset, with 3000 VQA evaluation Pairs, 8925 training Pairs, and six relevant subtasks. Then, we perform a
comprehensive assessment on various state-of-the-art proprietary and open-source MLLMs, e.g., DeepSeek-VL2, GPT-4o, Qwen2.5-VL, etc, and find that current MLLMs have weak abilities for this task. Further, in order to improve the intru13 sion understanding capabilities of current MLLMs, we propose a Post-Training Framework with three sequential training stages, i.e., Intrusion-aware Visual In15 struction Pre-training, Intrusion Chain of Thought tuning, and Intrusion-centric
VQA tuning, and sufficient experiments and comparisons are conducted to verify the effectiveness of the proposed three-stages training framework. All datasets, codes, and baselines will be publicly available.
