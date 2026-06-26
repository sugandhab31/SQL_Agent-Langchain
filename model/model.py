import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_model():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    return model