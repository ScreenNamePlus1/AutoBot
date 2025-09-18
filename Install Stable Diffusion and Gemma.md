# Local AI Models Installation Guide

This guide provides step-by-step instructions for installing and running popular open-source AI models locally on a Windows machine: **Stable Diffusion** (image generation), **Gemma**, **Llama 3**, **Mistral**, and **Phi 3** (text generation LLMs). These are sourced from Hugging Face. **Grok** (from xAI) is not locally installable but is included for clarity. The process is adaptable to macOS/Linux with minor changes (e.g., use `source .venv/bin/activate` for activation).

## Notes
- **Platform**: Focus is on Windows 10/11 (64-bit). 
- **Hardware**: Models can run on CPU, but a GPU (NVIDIA with CUDA) is recommended for performance.
- **Gated Models**: Gemma and Llama require accepting terms on Hugging Face and a valid access token.
- **Ethics Warning**: Use responsibly—models may generate biased, inaccurate, or harmful content. Ensure compliance with applicable laws and ethical guidelines.
- **Training Warning**: This guide covers **inference** (generating outputs), not training or fine-tuning, which requires significantly more resources (e.g., 80GB+ VRAM, large datasets, and advanced setup). Training instructions are beyond this scope; ask for specific guidance if needed.
- **Troubleshooting**: Ensure Hugging Face token is set (`huggingface-cli login`) and Python paths are correct.
- **Date**: Instructions are current as of September 18, 2025.
- **No-Code Alternative**: Tools like Ollama or LM Studio offer GUI-based setups.

## README: System Requirements

### Individual Model Requirements
Each model’s requirements for **inference** (generating outputs, not training) are listed below. Disk space includes model weights and virtual environment. CPU and RAM assume typical usage (e.g., one image or text generation at a time).

#### Stable Diffusion 3.5 Large
- **Disk Space**: ~10GB (model weights ~8GB, venv ~2GB).
- **CPU**: 
  - Minimum: Multi-core processor (e.g., Intel i5, AMD Ryzen 5, 4+ cores).
  - Recommended: Intel i7/Ryzen 7 for faster CPU fallback.
- **RAM**: 
  - Minimum: 8GB (CPU-only, slow).
  - Recommended: 16GB (with GPU, ~6GB VRAM used).
- **GPU**: NVIDIA RTX 3060+ (8GB+ VRAM) for CUDA acceleration. CPU-only is slow (~1-2 minutes per image).
- **Notes**: Quantization (e.g., FP16) reduces memory needs. Higher VRAM allows larger batch sizes.

#### Gemma-2-9B-IT
- **Disk Space**: ~18GB (model weights ~16GB, venv ~2GB).
- **CPU**: 
  - Minimum: Multi-core processor (e.g., Intel i5, AMD Ryzen 5, 4+ cores).
  - Recommended: Intel i7/Ryzen 7 for CPU-only inference.
- **RAM**: 
  - Minimum: 12GB (CPU-only, 4-bit quantization).
  - Recommended: 16GB+ (with GPU, ~10GB VRAM used).
- **GPU**: NVIDIA RTX 3060+ (12GB+ VRAM) for unquantized inference. 4-bit quantization enables lower-end GPUs.
- **Notes**: Quantization (via bitsandbytes) reduces memory footprint significantly.

#### Llama-3.2-3B-Instruct
- **Disk Space**: ~6GB (model weights ~4GB, venv ~2GB).
- **CPU**: 
  - Minimum: Dual-core processor (e.g., Intel i3, AMD equivalent).
  - Recommended: Intel i5/Ryzen 5 for decent performance.
- **RAM**: 
  - Minimum: 8GB (CPU-only, quantized).
  - Recommended: 12GB (with GPU, ~4GB VRAM used).
- **GPU**: NVIDIA GTX 1660+ (6GB+ VRAM) for acceleration. CPU-only is viable for this smaller model.
- **Notes**: Lightweight model, ideal for low-end systems.

#### Mistral-7B-Instruct-v0.3
- **Disk Space**: ~14GB (model weights ~12GB, venv ~2GB).
- **CPU**: 
  - Minimum: Multi-core processor (e.g., Intel i5, AMD Ryzen 5).
  - Recommended: Intel i7/Ryzen 7 for CPU-only.
- **RAM**: 
  - Minimum: 10GB (CPU-only, quantized).
  - Recommended: 16GB (with GPU, ~8GB VRAM used).
- **GPU**: NVIDIA RTX 3060+ (8GB+ VRAM) for unquantized inference.
- **Notes**: Efficient model; quantization helps on lower-end hardware.

#### Phi-3-mini-4k-instruct
- **Disk Space**: ~7GB (model weights ~5GB, venv ~2GB).
- **CPU**: 
  - Minimum: Dual-core processor (e.g., Intel i3, AMD equivalent).
  - Recommended: Intel i5/Ryzen 5 for faster inference.
- **RAM**: 
  - Minimum: 8GB (CPU-only, quantized).
  - Recommended: 12GB (with GPU, ~4GB VRAM used).
- **GPU**: NVIDIA GTX 1660+ (4GB+ VRAM) or CPU-only for quantized models.
- **Notes**: Highly optimized for small systems; GGUF versions further reduce requirements.

#### Grok
- **Disk Space**: Not applicable (not locally installable).
- **CPU/RAM/GPU**: Not applicable; runs via xAI’s servers or API.
- **Requirements**: Internet connection and xAI API access (Hugging Face token not required).
- **Notes**: See https://x.ai/api for programmatic access.

### Running All Models Simultaneously
Running all models (Stable Diffusion, Gemma, Llama 3, Mistral, Phi 3) concurrently (e.g., in separate processes or scripts) is resource-intensive. Requirements assume models are loaded in memory simultaneously, which may require sequential loading/unloading on consumer hardware.

- **Disk Space**: ~55GB total (~10GB Stable Diffusion + ~18GB Gemma + ~6GB Llama + ~14GB Mistral + ~7GB Phi 3). Add ~10GB buffer for temporary files.
- **CPU**: 
  - Minimum: High-end multi-core processor (e.g., Intel i9, AMD Ryzen 9, 12+ cores) to handle parallel tasks.
  - Recommended: Server-grade CPU (e.g., AMD EPYC, Intel Xeon) for smooth multi-model inference.
- **RAM**: 
  - Minimum: 64GB (assuming quantization for LLMs; ~10GB Stable Diffusion + ~12GB Gemma + ~4GB Llama + ~8GB Mistral + ~4GB Phi 3 + system overhead).
  - Recommended: 128GB to avoid swapping.
- **GPU**: 
  - Minimum: NVIDIA RTX 3090/4090 (24GB VRAM) to load all models concurrently with quantization.
  - Recommended: Multiple GPUs (e.g., 2x RTX 4090 or A100 40GB) for unquantized models.
- **Notes**: 
  - Simultaneous running is impractical on most consumer PCs due to VRAM/RAM limits. Use model offloading (e.g., `accelerate`) or run sequentially.
  - SSD recommended for faster loading; HDDs are slower but viable.
  - Power: GPUs may draw 600W+ combined; ensure adequate PSU and cooling.

### General Notes
- **GPU Compatibility**: NVIDIA GPUs with CUDA 11.8+ are ideal. Check with `nvidia-smi`. AMD/Intel GPUs may work with ROCm/OpenVINO but require extra setup.
- **OS**: Windows 10/11 (64-bit). macOS 12+ or Linux (Ubuntu 20.04+) are similar (adjust paths/commands).
- **Internet**: Required for initial model downloads (cached locally afterward).
- **Power/Cooling**: High-end GPUs require 300W+ each and good ventilation.
- **Training**: Not covered; requires significantly more resources (e.g., 80GB+ VRAM, large datasets). Request specific training guides if needed.

## Part 1: Prerequisites
These steps apply to all models. Complete them first.

    # Install Python 3.10.6
    # 1. Go to https://www.python.org/downloads/release/python-3106/
    # 2. Download Windows 64-bit installer
    # 3. Run installer, check "Add Python to PATH", complete installation
    # 4. Verify in Command Prompt:
    python --version
    # Should show 3.10.6

    # Install Git for Windows
    # 1. Go to https://git-scm.com/download/win
    # 2. Download and run installer, accept defaults
    # 3. Verify:
    git --version

    # Set Up Hugging Face Account and Token
    # 1. Create account at https://huggingface.co
    # 2. Go to Profile > Settings > Access Tokens, create read token, copy it
    # 3. Install CLI:
    pip install huggingface_hub
    # 4. Login:
    huggingface-cli login
    # Paste token when prompted

    # Install PyTorch (for acceleration)
    # CPU-only:
    pip install torch torchvision torchaudio
    # GPU (CUDA, adjust cu121 for your version; check with nvidia-smi):
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

## Part 2: Stable Diffusion (Image Generation)
Installs **Stable Diffusion 3.5 Large** for text-to-image generation using Hugging Face’s Diffusers.

    # Create Project Folder
    mkdir C:\AI_Projects\stable_diffusion
    cd C:\AI_Projects\stable_diffusion

    # Set Up Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate

    # Install Libraries
    pip install diffusers["torch"] transformers accelerate safetensors

    # Download and Run Stable Diffusion 3.5 Large
    # 1. Visit https://huggingface.co/stabilityai/stable-diffusion-3.5-large, accept terms
    # 2. Ensure logged in via huggingface-cli login
    # 3. Save as run_sd.py:

from diffusers import StableDiffusion3Pipeline
import torch

pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3.5-large",
    torch_dtype=torch.bfloat16
)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

prompt = "A futuristic cityscape at sunset, cyberpunk style"
image = pipe(prompt).images[0]
image.save("generated_image.png")

    # Run:
    python run_sd.py
    # Output: generated_image.png
    # Tips: Add pipe.enable_model_cpu_offload() for low VRAM. Expect ~10GB disk usage.

## Part 3: Gemma (Text Generation LLM)
Installs **Gemma-2-9B-IT**, Google’s open-weight LLM.

    # Create Project Folder
    mkdir C:\AI_Projects\gemma
    cd C:\AI_Projects\gemma

    # Set Up Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate

    # Install Libraries
    pip install -U transformers accelerate bitsandbytes

    # Download and Run Gemma-2-9B-IT
    # 1. Visit https://huggingface.co/google/gemma-2-9b-it, accept terms
    # 2. Ensure logged in
    # 3. Save as run_gemma.py:

import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="google/gemma-2-9b-it",
    torch_dtype=torch.bfloat16,
    device="cuda" if torch.cuda.is_available() else "cpu"
)

messages = [{"role": "user", "content": "Explain quantum computing in simple terms."}]
outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"][-1]["content"].strip())

    # Run:
    python run_gemma.py
    # Tips: For low memory, add model_kwargs={"quantization_config": {"load_in_4bit": True}} in pipeline. Expect ~18GB disk usage.

## Part 4: Llama 3 (Text Generation LLM)
Installs **Llama-3.2-3B-Instruct**, Meta’s lightweight LLM.

    # Create Project Folder
    mkdir C:\AI_Projects\llama
    cd C:\AI_Projects\llama

    # Set Up Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate

    # Install Libraries
    pip install -U transformers accelerate

    # Download and Run Llama-3.2-3B-Instruct
    # 1. Visit https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, accept terms, submit contact info
    # 2. Ensure logged in
    # 3. Save as run_llama.py:

import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-3B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]
outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"][-1]["content"])

    # Run:
    python run_llama.py
    # Tips: Use quantization for larger variants (e.g., 70B). Expect ~6GB disk usage.

## Part 5: Mistral (Text Generation LLM)
Installs **Mistral-7B-Instruct-v0.3**, an efficient LLM.

    # Create Project Folder
    mkdir C:\AI_Projects\mistral
    cd C:\AI_Projects\mistral

    # Set Up Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate

    # Install Libraries
    pip install -U transformers mistral_inference

    # Download and Run Mistral-7B-Instruct-v0.3
    # 1. No gating required
    # 2. Download model files:

from huggingface_hub import snapshot_download
from pathlib import Path

mistral_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
mistral_path.mkdir(parents=True, exist_ok=True)
snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"],
    local_dir=mistral_path
)

    # 3. Save as run_mistral.py:

from transformers import pipeline

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
]
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
response = chatbot(messages)
print(response[0]["generated_text"][-1]["content"])

    # Run:
    python run_mistral.py
    # CLI alternative:
    mistral-chat %HOMEPATH%\mistral_models\7B-Instruct-v0.3 --instruct --max_tokens 256
    # Tips: Expect ~14GB disk usage.

## Part 6: Phi 3 (Text Generation LLM)
Installs **Phi-3-mini-4k-instruct**, Microsoft’s efficient LLM.

    # Create Project Folder
    mkdir C:\AI_Projects\phi
    cd C:\AI_Projects\phi

    # Set Up Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate

    # Install Libraries
    pip install transformers==4.41.2 torch==2.3.1 accelerate==0.31.0 flash_attn==2.5.8

    # Download and Run Phi-3-mini-4k-instruct
    # 1. No gating required
    # 2. Save as run_phi.py:

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="cuda" if torch.cuda.is_available() else "cpu",
    torch_dtype="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2"
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Solve 2x + 3 = 7."}
]
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
output = pipe(messages, max_new_tokens=500, return_full_text=False, temperature=0.0, do_sample=False)
print(output[0]['generated_text'])

    # Run:
    python run_phi.py
    # Tips: Use GGUF versions for quantized, CPU-friendly models. Expect ~7GB disk usage.

## Part 7: Grok (Not Locally Installable)
Grok, created by xAI, is not available for local installation (proprietary architecture).

    # Access Grok
    # 1. Use via https://grok.com, https://x.com, or Grok iOS/Android apps (free with quotas)
    # 2. For programmatic access:
    #    - See https://x.ai/api for xAI API details
    #    - Requires internet and API key (not Hugging Face token)
    # No local disk/CPU/RAM requirements.

## Additional Notes
- **Expanding to Other Models**: For models like Whisper (speech-to-text) or CLIP (image-text), use `transformers` or `diffusers` with `from_pretrained(model_id)`. Search Hugging Face for model IDs.
- **No-Code Option**: Ollama or LM Studio offer GUI-based local AI setups—download from their official sites.
- **Troubleshooting**:
  - Dependency conflicts? Use specified versions (e.g., `transformers==4.41.2` for Phi 3).
  - CUDA errors? Match PyTorch CUDA version with `nvidia-smi` output.
  - Slow inference? Use quantization (e.g., `bitsandbytes`) or smaller models.
- **Training**: Not covered due to high resource demands (e.g., 80GB+ VRAM). Request specific fine-tuning guides if needed.
