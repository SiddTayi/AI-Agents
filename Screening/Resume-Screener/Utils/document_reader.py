from Utils.file_reader import read_resume_and_jd
from Commons.config import RESUME_PATH, JD_PATH
import os

def get_resume_and_jd(use_langchain: bool = False):
    """
    Read the resume and job description files using paths from config.
    
    Args:
        use_langchain (bool): Whether to use LangChain loader for PDFs
        
    Returns:
        tuple: (resume_text, jd_text) - extracted text from both files
    """
    # Check if files exist
    if not os.path.exists(RESUME_PATH):
        print(f"❌ Resume file not found: {RESUME_PATH}")
        return None, None
    
    if not os.path.exists(JD_PATH):
        print(f"❌ Job description file not found: {JD_PATH}")
        return None, None
    
    # Extract text from both files
    resume, jd = read_resume_and_jd(RESUME_PATH, JD_PATH, use_langchain)
    
    # Print status
    if resume:
        print(f"✅ Resume extracted successfully! Length: {len(resume)} characters")
    else:
        print("❌ Failed to extract resume text")
    
    if jd:
        print(f"✅ Job Description extracted successfully! Length: {len(jd)} characters")
    else:
        print("❌ Failed to extract job description text")
    
    return resume, jd

def get_resume_and_jd_with_langchain():
    """
    Get resume and job description using LangChain loaders for better text extraction.
    
    Returns:
        tuple: (resume_text, jd_text) - extracted text from both files
    """
    return get_resume_and_jd(use_langchain=True)

# If you want to test this directly
if __name__ == "__main__":
    print("Testing with PyMuPDF...")
    resume, jd = get_resume_and_jd(use_langchain=False)
    
    if resume:
        print("\n📄 Resume preview (first 300 characters):")
        print("-" * 50)
        print(resume[:300] + "..." if len(resume) > 300 else resume)
        print("-" * 50)
    
    if jd:
        print("\n📄 Job Description preview (first 300 characters):")
        print("-" * 50)
        print(jd[:300] + "..." if len(jd) > 300 else jd)
        print("-" * 50)
    
    print("\n" + "="*60)
    print("Testing with LangChain...")
    resume_lc, jd_lc = get_resume_and_jd(use_langchain=True)
    
    if resume_lc:
        print("\n📄 Resume preview (LangChain) (first 300 characters):")
        print("-" * 50)
        print(resume_lc[:300] + "..." if len(resume_lc) > 300 else resume_lc)
        print("-" * 50)
    
    if jd_lc:
        print("\n📄 Job Description preview (LangChain) (first 300 characters):")
        print("-" * 50)
        print(jd_lc[:300] + "..." if len(jd_lc) > 300 else jd_lc)
        print("-" * 50) 