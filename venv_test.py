import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Use the api_key in your OpenAI calls
print("API Key", api_key)
