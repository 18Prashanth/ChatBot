import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("models/gemini-2.5-flash-preview-05-20")

def get_gemini_response(message: str) -> str:
    response = model.generate_content(message)
    return response.text.strip()
