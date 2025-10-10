
import os
from dotenv import load_dotenv
from google import genai

# Load the environment file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found. Make sure .env file is loaded.")

# Load your API key
client = genai.Client(api_key=api_key)

print("Fetching available models...\n")

# List all models your API key can access
models = client.models.list()

for m in models:
    print(m.name)
