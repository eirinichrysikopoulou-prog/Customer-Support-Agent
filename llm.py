from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=GEMINI_API_KEY,
)