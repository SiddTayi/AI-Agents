import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.document_reader import get_resume_and_jd, get_resume_and_jd_with_langchain
from agent_def import resume_parser, hiring_manager
from task_def import resume_task, hiring_task
from crewai import Crew

def main():
    print("📄 Reading documents...")
    # Method 1: Using PyMuPDF (faster, good for most PDFs)
    resume, jd = get_resume_and_jd(use_langchain=False)
    # Method 2: Using LangChain (better for complex PDFs with tables, forms)
    # resume, jd = get_resume_and_jd_with_langchain()
    
    if resume and jd:
        print(f"✅ Successfully loaded documents:")
        print(f"   📄 Resume: {len(resume)} characters")
        print(f"   📄 Job Description: {len(jd)} characters")
        
        # Create agents
        print("\n🤖 Creating agents...")
        resume_agent = resume_parser()
        hiring_agent = hiring_manager()
        
        # Create tasks
        print("📋 Creating tasks...")
        resume_analysis_task = resume_task(resume_agent, resume)
        hiring_evaluation_task = hiring_task(hiring_agent, jd, resume, None)  # context is None for now

        # Create crew
        print("👥 Creating crew...")
        crew = Crew(
            agents= [hiring_agent], #[resume_agent, hiring_agent],
            tasks= [hiring_evaluation_task], #[resume_analysis_task, hiring_evaluation_task],
            verbose=True,
            memory=False  
        )
        
        # Execute the crew
        print("🚀 Starting crew execution...")
        result = crew.kickoff()
        
        print("\n📊 Crew Results:")
        print("=" * 50)
        print(result)
        print("=" * 50)
        
        return resume, jd, result
    else:
        print("❌ Failed to load documents")
        return None, None, None

if __name__ == "__main__":
    resume_text, jd_text, crew_result = main()
