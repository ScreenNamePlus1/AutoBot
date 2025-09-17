Wanting to install local help? Train your own models? No problem. Here are the step-by-step instructions for installing Stable Diffusion and Gemma with Hugging Face, properly formatted with code blocks for readability and easy copying.
Part 1: Prerequisites
Before you begin, you need to install a few essential tools.
 * Install Python 3.10.6:
   * Go to the official Python website.
   * Download the Windows installer for the 64-bit version.
   * Run the installer. On the first screen, make sure to check the box that says "Add Python to PATH".
   * Complete the installation.
 * Install Git for Windows:
   * Go to the Git for Windows website.
   * Download and run the installer. You can generally accept all the default options.
 * Get a Hugging Face Account and Access Token:
   * Go to the Hugging Face website and create a free account.
   * Go to your profile settings, navigate to "Access Tokens," and create a new token. Copy this token; you will need it later.
Part 2: Installing and Running Stable Diffusion
This process uses a Python script to download and run the Stable Diffusion model.
 * Create a Project Folder:
   * Create a new folder on your computer for this project (e.g., C:\AI_Projects\stable_diffusion).
 * Open Command Prompt and Create a Virtual Environment:
   * Open the Start Menu and type cmd. Open the Command Prompt app.
   * Navigate to your new project folder using the cd command. For example, cd C:\AI_Projects\stable_diffusion.
   * Create a virtual environment by running:
     python -m venv .venv

   * Activate the environment:
     .venv\Scripts\activate

     You'll know it's active when you see (.venv) at the beginning of your command prompt line.
 * Install the Necessary Libraries:
   * Run the following command to install the Hugging Face diffusers and transformers libraries, as well as PyTorch.
     pip install diffusers transformers accelerate torch

 * Create a Python Script:
   * In your project folder, create a new file named generate_image.py and open it with a text editor.
   * Copy and paste the following code into the file:
   <!-- end list -->
   from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion v1.5 model
# It will be downloaded to your cache the first time you run this
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Move the model to your GPU for faster processing
if torch.cuda.is_available():
    pipe = pipe.to("cuda")

# Define your text prompt
prompt = "a photo of an astronaut riding a horse on a realistic planet"

# Generate the image
image = pipe(prompt).images[0]

# Save the generated image
image.save("astronaut_horse.png")

print("Image saved as astronaut_horse.png")

 * Run the Script:
   * Save the file.
   * In your Command Prompt (with the virtual environment still active), run the script with the command:
     python generate_image.py

   * The script will download the model (this will take a while the first time) and then generate your image. Once finished, you will find astronaut_horse.png in your project folder.
Part 3: Installing and Running Gemma
This process is similar to Stable Diffusion, but with a different model and pipeline.
 * Create a New Project Folder:
   * Create a new folder for this project (e.g., C:\AI_Projects\gemma_llm).
 * Open Command Prompt and Create a Virtual Environment:
   * Open a new Command Prompt window and navigate to your new folder.
   * Create and activate a new virtual environment:
     python -m venv .venv

     .venv\Scripts\activate

 * Install the Necessary Libraries:
   * Run the following command to install the required libraries. This includes bitsandbytes, which is essential for running Gemma efficiently on a GPU.
     pip install transformers accelerate bitsandbytes torch

 * Log in to Hugging Face:
   * In the Command Prompt, run:
     huggingface-cli login

   * Paste your access token that you copied earlier when prompted.
 * Create a Python Script:
   * Create a new file in your folder named gemma_chat.py.
   * Copy and paste the following code:
   <!-- end list -->
   from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# The model name for Gemma 2B
model_id = "google/gemma-2b-it"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

# Define a prompt for the model
prompt = "What is the capital of France?"

# Tokenize the prompt
input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate a response
outputs = model.generate(**input_ids, max_new_tokens=200)

# Decode the output and print the response
print(tokenizer.decode(outputs[0]))

 * Run the Script:
   * Save the file.
   * In your Command Prompt, run the script with the command:
     python gemma_chat.py

   * The model will download, and after a moment, the response will be printed to your command prompt.

---

**Installing and running Stable Diffusion and Gemma on a 32-bit Windows machine is not officially supported and will likely not work due to hardware limitations. These models require a 64-bit operating system and a powerful GPU with a 64-bit architecture to run efficiently. The models themselves, as well as the PyTorch and diffusers libraries, are built for 64-bit systems.*

---

**​The previous instructions assumed a 64-bit Windows 11 installation, as Windows 11 is exclusively 64-bit. There is no official 32-bit version of Windows 11. Most modern deep learning frameworks, including the ones used by Hugging Face, are designed for the more common and powerful 64-bit hardware.
​There are no separate 32-bit installation files or procedures because the necessary software stack does not exist for 32-bit machines.*
