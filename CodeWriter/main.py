import requests
from autogen import AssistantAgent, UserProxyAgent

# --- Ollama model settings ---
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen2.5:14b"

# LLM config for Autogen
llm_config = {
    "config_list": [
        {
            "model": MODEL_NAME,
            "base_url": OLLAMA_BASE_URL,
            "api_type": "ollama"  # important: tells autogen it's an Ollama model
        }
    ]
}

# Create coding assistant (using Ollama locally)
coder = AssistantAgent(
    name="Coder",
    llm_config=llm_config
)

# Executor agent to run code and return errors/output
executor = UserProxyAgent(
    name="Executor",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)

# Error-correcting coding loop
def coding_loop(task, max_rounds=5):
    print(f"💡 Task: {task}")
    coder.initiate_chat(executor, message=task)

if __name__ == "__main__":
    coding_loop("Write Python code to generate the first 20 Fibonacci numbers.")
