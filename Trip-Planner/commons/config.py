import os 
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL")
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")