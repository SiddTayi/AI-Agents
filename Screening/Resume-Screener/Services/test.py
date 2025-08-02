import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI


ollama_llm = ChatOpenAI(
    model="ollama/llama3.2",  
    base_url="http://localhost:11434",
    api_key="ollama",
    temperature=0.7 
)

# 2. Define an Agent
researcher = Agent(
    role="Senior AI Researcher",
    goal="Discover cutting-edge advancements in AI and provide a concise summary.",
    backstory="You are a highly experienced AI researcher known for your ability to "
              "identify significant breakthroughs and explain them clearly.",
    verbose=True, 
    allow_delegation=False, 
    llm=ollama_llm 
)

# 3. Define a Task
research_task = Task(
    description=(
        "Research the latest news and advancements in generative AI, focusing on "
        "new model architectures, applications, and ethical considerations. "
        "Summarize the top 3 most impactful developments in a paragraph."
    ),
    expected_output="A concise paragraph summarizing the top 3 most impactful "
                    "developments in generative AI, including new model "
                    "architectures, applications, and ethical considerations.",
    agent=researcher,
    output_file="research_summary.md"
)

# 4. Create a Crew (even with one agent, it's still a "crew")
single_agent_crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential, 
    verbose=True 
)

# 5. Kick off the crew
print("## Starting the AI Research Crew ##")
result = single_agent_crew.kickoff()

print("\n\n##################################")
print("## Research Summary Completed ##")
print("##################################")
print(result)