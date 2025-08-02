import os
from langchain_openai import ChatOpenAI

RESUME_PATH = "Files/res2.pdf"
JD_PATH = "Files/ETL_jd.docx"
LLM = ChatOpenAI(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    api_key="ollama",
    temperature=0.7
)