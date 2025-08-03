import os
from langchain_openai import ChatOpenAI

# Get the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

RESUME_PATH = os.path.join(project_root, "Files/res2.pdf")
JD_PATH = os.path.join(project_root, "Files/ETL_jd.docx")
LLM = ChatOpenAI(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    api_key="ollama",
    temperature=0.7
)