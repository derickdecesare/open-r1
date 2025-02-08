# GRPO config file

recipes/deepseek/config_base_math_smallr.yaml

# GRPO training scrip

src/grpo.py

# Deepseek zeRO-2 config

recipes/accelerate_configs/zero2.yaml

# GRPO slurm script (used to launch the training job on a cluster)

slurm/grpo.slurm

# Eval script? where is this?

src/open_r1/evaluate.py

# Project dependecies where is this?

setup.py

0.

- Make evaluate dataset and do some basic testing on reward functions to ensure they work

1. Training setup

- Rent a pod with 8x H100s
- Use a PyTorch/CUDA base image
- Clone the repo and install dependencies
- Instead of the SLURM script, you would directly run:
  ACCELERATE_LOG_LEVEL=info accelerate launch \
   --config_file recipes/accelerate_configs/zero2.yaml \
   --num_processes 7 \
   src/open_r1/grpo.py \
   --config recipes/deepseek/DeepSeek-R1-Distill-Qwen-7B/grpo/config_base_math_smalllr.yaml

This is ONE command btw:

accelerate launch \
 [accelerate options] \ # Options for distributed setup
your_script.py \ # The script to run
[script arguments] # Arguments for your script

3. Evaluation (Same RunPod Session)
   - Run evaluation before shutting down GPUs:
   ```bash
   make evaluate MODEL=your-trained-model TASK=math_500
   ```
   - Or use the direct lighteval command if preferred

# Docker notes

1. Testing locally

# Build and start

docker-compose up -d --build

# Connect to running container:

docker-compose exec open-r1 bash

2. Push to Docker Hub

# Tag the image (replace with your Docker Hub username)

docker tag open-r1_open-r1 yourusername/open-r1:latest

# Push to Docker Hub

docker push yourusername/open-r1:latest
