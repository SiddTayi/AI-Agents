from crewai import Agent
from Commons.config import LLM

llm = LLM

# Agent 1 Parse resume
def resume_parser():
    return Agent(
        role = "Resume Analyzer - Hiring Manager",
        goal = "Analyze and identify key strengths from the resume for hiring process",
        backstory = """
            You are an expert in analyzing the resume and identifying key strengths such as:
            1. Tech stack: Identify all the technical skills from the resume - be it in experience, skills, and projects section.  
            2. Experience: Analyze the experience and extract key points such as the tech stack used, the impact, work done, etc. 
            3. Projects: If there are any projects, extract information from the projects such as the tech stack used, the impact, work done, etc. 
            4. Certification - if any
            5. Education - if any
            6. Experience in years
            7. Graduation dates and timeline (in years)
            Extract other key information if seen other than these.  
        """,
        verbose = True,
        llm = llm
    )

def hiring_manager():
    return Agent(
        role = "Hiring Manager",
        goal = "Analyze the candidate's resume with the JD and assign a score out of 10.",
        backstory = """
            - You are a highly experienced hiring manager. You are responsible to analyze and compare the resume with the JD: job description, and assign a score out of 10. 
            - You tend to use industry standard practices to consider a candidate with no bias and discrimination.  
        """,
        verbose = True,
        llm  = llm
    )