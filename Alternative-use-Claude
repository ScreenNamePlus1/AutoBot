// Claude-API-Guide
# Local AI Models Installation Guide

**You are going to need to buy an API key and Claude is rated M. Not R. Definitely not XXX.**

This guide provides step-by-step instructions for installing and running Claude on a computer and mobile device. Claude is a large language model created by Anthropic, accessed via an API (Application Programming Interface). This means it runs on remote servers, so it does not require a powerful local GPU.

## Notes
- **Platform**: Focus is on a standard computer running Windows 11 (64-bit) and a mobile device running Termux (Android).
- **Hardware**: Minimal hardware requirements since the model runs on Anthropic's cloud servers.
- **API Key**: An API key from Anthropic is required for access. Billing information may be required to get an API key.
- **Ethics Warning**: Use responsibly—models may generate biased, inaccurate, or harmful content. Ensure compliance with applicable laws and ethical guidelines.
- **Date**: Instructions are current as of September 19, 2025.
- **No-Code Alternative**: The official Claude website offers a user-friendly chat interface with free access and paid plans.

## README: System Requirements

### Individual Model Requirements

#### Claude 3 Sonnet
- **Disk Space**: ~20MB for the Python virtual environment and scripts. No model weights are stored locally.
- **CPU**:
  - Minimum: Any modern multi-core processor.
- **RAM**:
  - Minimum: 2GB (for running the Python script).
- **GPU**: Not required for inference.
- **Notes**: All heavy computational work is handled by Anthropic's servers. Your local device only sends and receives data.

### Running a Python Script with Claude
The requirements for running a single Python script that calls the Claude API are extremely low, as the local machine is only handling the data transfer, not the model inference.

- **Disk Space**: ~200MB total.
- **CPU**: Any modern multi-core processor.
- **RAM**: 4GB recommended to run the OS, Termux/Terminal, and Python script comfortably.
- **GPU**: Not required.
- **Notes**: An internet connection is mandatory. Power and cooling are not a concern.

### General Notes
- **OS**: Windows 11 (64-bit). The instructions for Termux (Android) are also provided.
- **Internet**: Required for every API call.
- **Power/Cooling**: Not a concern for local device.
- **Training**: Not covered; requires a partnership with Anthropic or use of other tools.

## Part 1: Prerequisites
These steps apply to both Windows 11 and Termux.

    # Install Python 3.10 or later
    # 1. On Windows: Go to https://www.python.org/downloads/ and download the Windows installer. Make sure to check "Add Python to PATH" during installation.
    # 2. On Termux: Use the package manager.
    pkg install python
    
    # Install Git
    # 1. On Windows: Go to https://git-scm.com/download/win and run the installer.
    # 2. On Termux: Use the package manager.
    pkg install git

    # Set Up Anthropic Account and API Key
    # 1. Go to https://console.anthropic.com/ and create an account.
    # 2. Navigate to "API Keys" in the dashboard.
    # 3. Click "+ Create Key", name it, and copy the key.
    # 4. **Important**: Save this key securely. It cannot be viewed again.

## Part 2: Installing and Using the Claude API on Windows 11
This section guides you through the process on a Windows 11 computer.

    # 1. Create a project folder and navigate to it
    mkdir C:\AI_Projects\claude
    cd C:\AI_Projects\claude

    # 2. Set Up a Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate

    # 3. Install the Anthropic Python library
    pip install anthropic

    # 4. Set your API key as an environment variable for security
    # This is a one-time command per terminal session.
    set ANTHROPIC_API_KEY="your_api_key_here"

    # 5. Save the Python script (run_claude.py)
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain the difference between local and API-based models in a short paragraph."},
    ]
)

print(message.content[0].text)

    # 6. Run the script
    python run_claude.py

    # Expected Output: A paragraph explaining the difference between the models.

## Part 3: Installing and Using the Claude API on a Mobile Device (Termux)
This section guides you through the process on your mobile device.

    # 1. Create a project folder and navigate to it
    mkdir /data/data/com.termux/files/home/claude
    cd /data/data/com.termux/files/home/claude

    # 2. Set Up a Virtual Environment
    python -m venv .venv
    source .venv/bin/activate

    # 3. Install the Anthropic Python library
    pip install anthropic

    # 4. Set your API key as an environment variable
    # This is a one-time command per terminal session.
    export ANTHROPIC_API_KEY="your_api_key_here"

    # 5. Save the Python script (run_claude.py)
    # Use a text editor like nano or vim to create the file.
    # The code is the same as the Windows section.
    # For example, using nano:
    nano run_claude.py
    # Paste the code and save (Ctrl+O, Enter, Ctrl+X)

    # 6. Run the script
    python run_claude.py

    # Expected Output: A paragraph explaining the difference between the models.

