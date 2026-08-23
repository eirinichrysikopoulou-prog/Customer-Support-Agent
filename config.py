import os
from dotenv import load_dotenv
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
)
load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

CONFIDENCE_THRESHOLD = 0.75
