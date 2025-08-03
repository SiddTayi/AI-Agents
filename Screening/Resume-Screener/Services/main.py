import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.document_reader import get_resume_and_jd, get_resume_and_jd_with_langchain
from Utils.excel_manager import ExcelManager
from agent_def import resume_parser, hiring_manager
from task_def import resume_task, hiring_task
from crewai import Crew
from Commons.config import RESUME_PATH, JD_PATH

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
        
        # Initialize Excel manager
        excel_manager = ExcelManager()
        
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
        
        # Save results to Excel
        print("\n💾 Saving results to Excel...")
        success = excel_manager.append_result(RESUME_PATH, JD_PATH, result)
        
        if success:
            # Get and display summary statistics
            stats = excel_manager.get_summary_stats()
            if isinstance(stats, dict):
                print("\n📈 Summary Statistics:")
                print(f"   📊 Total Candidates: {stats['total_candidates']}")
                print(f"   📊 Average Score: {stats['average_score']:.2f}" if stats['average_score'] != 'N/A' else f"   📊 Average Score: {stats['average_score']}")
                print(f"   🎯 High Scores (8-10): {stats['high_scores']}")
                print(f"   📋 Medium Scores (6-7): {stats['medium_scores']}")
                print(f"   ⚠️ Low Scores (<6): {stats['low_scores']}")
            else:
                print(f"📈 {stats}")
        
        return resume, jd, result
    else:
        print("❌ Failed to load documents")
        return None, None, None

if __name__ == "__main__":
    resume_text, jd_text, crew_result = main()
