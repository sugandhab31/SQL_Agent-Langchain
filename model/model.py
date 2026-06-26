import os
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv(override=True)
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def get_model():
    # model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    # return model

    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        temperature=0.4,
        huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN
    )
    model = ChatHuggingFace(llm=llm)
    return model