import os
from dotenv import load_dotenv
from types import SimpleNamespace # Import the SimpleNamespace tool
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# --- 1. Setup ---
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# --- 2. Agent Configuration ---
# This configuration creates a powerful, general-purpose AI assistant
# with no personal context.
user_name = "Vivian"
# -- Persona and Rules --
# A simple, direct prompt that unlocks the AI's full capabilities.
prompt = """
You are Jarvis, a versatile and helpful AI assistant.

Your purpose is to provide accurate information, assist with a wide range of tasks, and engage in meaningful conversations. You are capable of understanding complex topics, writing, coding, brainstorming, and much more.

Always strive for clarity, accuracy, and neutrality in your responses. If you do not know an answer or cannot fulfill a request, clearly state your limitations.
"""

# -- Initial Greeting --
# A clean, generic greeting for a universal assistant.
first_message = "Hello! How can I help you today?"

# -- Initial Greeting --
# A more personal and context-aware first message.
first_message = f"Good evening, {user_name}. Jarvis here. How can I help you?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

client = ElevenLabs(api_key=API_KEY)

# --- 3. Create a Custom Configuration Object ---
# This is the workaround for the library's bug.
# We create a simple, unlocked object and manually add all the
# attributes that the internal code expects to find.

config = SimpleNamespace()
config.conversation_config_override = conversation_override
config.extra_body = {}
config.dynamic_variables = {}
config.user_id = None # The attribute that was causing all the crashes

# --- 4. Define Callback Functions ---
def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# --- 5. Create and Start the Conversation ---
# Pass our custom 'config' object to the conversation.
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()

# --- 6. Keep the Script Running ---
input("Assistant started. Press Enter to stop.\n")

conversation.end_session()

print("Assistant session ended.")