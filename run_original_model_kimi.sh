#!/bin/bash
####################
### 加载依赖模块环境 ###
#####################

# module load compilers/cuda/11.7
# module load nccl/2.18.3-1_cuda12.1
# module load compilers/gcc/12.2.0
# module load cudnn/8.9.5.29_cuda12.x
# module load tensorboard/2.11.2
# module load miniforge3/24.1
# module list
# conda list
# 正确激活conda环境
source $(conda info --base)/etc/profile.d/conda.sh  # source ~/miniconda3/etc/profile.d/conda.sh
conda activate mllm-isu
python your_path/predict_kimivl.py
