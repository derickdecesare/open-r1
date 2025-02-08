FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn8-runtime

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace/open-r1

# Install vLLM first (as recommended in README)
RUN pip install vllm==0.7.1

# Install specific dependencies that need to be pinned
RUN pip install torch==2.5.1 \
    deepspeed==0.15.4 \
    liger_kernel==0.5.2 \
    math-verify==0.5.2


# Install git dependencies
RUN pip install \
git+https://github.com/huggingface/lighteval.git@86f62259f105ae164f655e0b91c92a823a742724#egg=lighteval[math] \
git+https://github.com/huggingface/transformers.git@main \
git+https://github.com/huggingface/trl.git@main



# Install the package in editable mode with all extras (in setup.py)
RUN GIT_LFS_SKIP_SMUDGE=1 pip install -e ".[dev,eval,quality,tests]"

# Default command to keep container running # run time command
CMD ["tail", "-f", "/dev/null"]