ElevenLabs AI Voice Assistant 🤖

A powerful, real-time conversational voice assistant built in Python. This project uses the ElevenLabs API to create a voice-activated AI that you can talk to, ask questions, and get instant audible responses from.
The assistant's personality and knowledge base are fully customizable, allowing you to create anything from a specialized personal assistant to a general-knowledge AI.

## Features
Real-Time Voice Conversation: Speak to the assistant and get spoken replies instantly.

High-Quality Voice: Leverages ElevenLabs' state-of-the-art text-to-speech for natural and realistic voice output.

Fully Customizable Personality: The assistant's core persona, knowledge, and rules are defined in a simple text prompt, making it easy to modify.

General Knowledge Capable: Can be configured to answer a vast range of general knowledge questions, similar to other major LLMs.

Secure: Keeps your API keys safe using environment variables.

## Tech Stack
Python 3.8+

ElevenLabs Python SDK: The official library for interacting with the ElevenLabs API.

python-dotenv: For managing environment variables and API keys securely.

## Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.8 or higher

pip (Python package installer)

git (for cloning the repository)

An active ElevenLabs Account. You can sign up at elevenlabs.io.

Your ElevenLabs API Key, which can be found in your account's "Profile" section.

## 🔧 Installation & Setup
Follow these steps carefully to get the assistant running on your local machine.

1. Clone the Repository
Open your terminal and clone this repository to your desired location.

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
(Replace your-username/your-repository-name with your actual GitHub repository URL.)

2. Create a Python Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.

Bash

# Create the virtual environment
python -m venv env

# Activate the environment
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
3. Install Dependencies
This project uses a requirements.txt file to manage its packages. Run the following command to install them:

Bash

pip install -r requirements.txt
4. Set Up Your API Key
Your secret API key is stored in a .env file that you must create.

Create a new file in the root of the project directory named .env

Open the .env file and add your ElevenLabs API Key in the following format:

API_KEY="your_elevenlabs_api_key_here"
The .gitignore file is already configured to prevent this file from being uploaded to GitHub.

## 🚀 How to Use
With the setup complete, you can now run the assistant.

Ensure your virtual environment is active. (You should see (env) at the beginning of your terminal prompt).

Run the main script:

Bash

python voice_assistant.py
Start the Conversation: The script will print Assistant started. Press Enter to stop. and the assistant will speak its initial greeting.

After the greeting, speak clearly into your microphone.

The assistant will process your speech, think, and reply audibly. The conversation will also be transcribed in your terminal.

To stop the program, go to the terminal window and press the Enter key.

## 💡 Customizing the Assistant
The "brain" of your assistant is the prompt variable inside the voice_assistant.py script. You can edit this text to completely change its personality, knowledge, and behavior.

Example: General Knowledge AI (Current Configuration)
Python

prompt = """
You are Aura, a versatile and helpful AI assistant.
Your purpose is to provide accurate information, assist with a wide range of tasks, and engage in meaningful conversations...
"""
This prompt creates a powerful, all-purpose assistant.

Example: Specialized Personal Assistant
You could change the prompt to create a highly focused personal assistant, as we did in earlier versions:

Python

# You would need to add your variables (user_name, schedule, etc.) back for this
prompt = f"""
You are a proactive personal assistant for {user_name}.
Your knowledge is strictly limited to the following information:
- Today's Schedule: {schedule}
- Active Task List: {task_list}

If you are asked for information you don't have, you must reply: "I don't have access to that."
"""
By editing this prompt, you can make the assistant anything you want it to be. Experiment and have fun!
