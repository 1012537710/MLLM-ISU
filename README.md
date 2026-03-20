<div align="center">

# MLLM-ISU: The First-Ever Comprehensive Benchmark for Multimodal Large Language Models based Intrusion Scene Understanding

## NeurIPS 2025

[**[📖 Paper]**](https://openreview.net/forum?id=3wJh9Pw2sn) | [**[🤗 Hugging Face]**](https://huggingface.co/Xukun666)

</div>

## 0. Introduction
Vision-based intrusion detection has multiple applications in practical scenarios, e.g., autonomous driving, intelligent monitoring, and security. Previous works mainly focus on improving the intrusion detection performance, without a comprehensive and in-depth understanding of the intrusion scene. To fill this gap, we explore a novel task called Multimodal Large Language Models based Intrusion Scene Understanding (MLLM-ISU) and report a comprehensive benchmark for the task. Specifically, we first design an effective and automatic visual question-answer generation strategy, constructing a new MLLM-ISU dataset, with **3000** VQA evaluation Pairs, **8925** training Pairs, and six relevant subtasks. Then, we perform a comprehensive assessment on various state-of-the-art proprietary and open-source MLLMs, e.g., DeepSeek-VL2, GPT-4o, Qwen2.5-VL, etc, and find that current MLLMs have weak abilities for this task. Further, in order to improve the intrusion understanding capabilities of current MLLMs, we propose a Post-Training Framework with three sequential training stages, i.e., Intrusion-aware Visual Instruction Pre-training, Intrusion Chain of Thought tuning, and Intrusion-centric VQA tuning, and sufficient experiments and comparisons are conducted to verify the effectiveness of the proposed three-stages training framework.

## 🌟 Highlights
* **First-Ever Benchmark**: Specifically designed for **Intrusion Scene Understanding (ISU)** in complex environments.
* **Comprehensive Evaluation**: Benchmarking 10+ state-of-the-art MLLMs (e.g., Qwen2.5-VL, InternVL2) using their official implementations.
* **Real-world Scenarios**: Covering diverse intrusion cases with high-quality multimodal data.


## 🚀 Quick Start

We provide a step-by-step guide to help you reproduce the evaluation results for MLLM-ISU. Here, we use Kimi-VL as a primary example. Our testing environment is based on [**[**ModelScope**]**](https://modelscope.cn/home).

# S1. Environment Setup

First, create a clean Conda environment and install the necessary dependencies as specified in requirements.txt.

1. Create a new conda environment
```
conda create -n mllm-isu python=3.10 -y
```

2. Activate the environment
```
conda activate mllm-isu
```

3. Install dependencies using TUNA mirror for faster download
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# S2. Model Weight Preparation

1. Install modelscope
```
pip install modelscope
```

2. Download

```
modelscope download --model moonshotai/Kimi-VL-A3B-Instruct
```

# S3. Running Inference

To reproduce our results on a Slurm cluster, use the provided submission script:

```
# Submit the job with 4 GPUs
sbatch -N 1 --gres=gpu:4 -p vip_gpu_ailab -A ai4bio run_original_model_kimi.sh
```

## 📝 Citation

If you find our work or dataset helpful, please consider citing:

```bibtex
@inproceedings{hanmllm,
  title={MLLM-ISU: The First-Ever Comprehensive Benchmark for Multimodal Large Language Models based Intrusion Scene Understanding},
  author={Han, Fujun and Ye, Peng},
  booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks Track}
}
