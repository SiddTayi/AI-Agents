import fitz  # PyMuPDF
import os
from typing import Optional, List
from docx import Document  # python-docx for .docx files
from langchain_community.document_loaders import PyMuPDFLoader as pfl

def extract_text_from_pdf_pymupdf(pdf_path: str) -> Optional[str]:
    """
    Extract text from a PDF file using PyMuPDF (fitz).
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF, or None if extraction fails
    """
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        text = ""
        
        # Extract text from each page
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        doc.close()
        return text.strip()
    
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {str(e)}")
        return None

def extract_text_from_pdf_langchain(pdf_path: str) -> Optional[str]:
    """
    Extract text from a PDF file using LangChain PyMuPDFLoader.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF, or None if extraction fails
    """
    try:
        # Use LangChain PyMuPDFLoader
        loader = pfl(pdf_path)
        documents = loader.load()
        
        # Combine all pages
        text = ""
        for doc in documents:
            text += doc.page_content + "\n"
        
        return text.strip()
    
    except Exception as e:
        print(f"Error extracting text from {pdf_path} using LangChain: {str(e)}")
        return None

def extract_text_from_docx(docx_path: str) -> Optional[str]:
    """
    Extract text from a Word document (.docx) file using python-docx.
    
    Args:
        docx_path (str): Path to the .docx file
        
    Returns:
        str: Extracted text from the .docx file, or None if extraction fails
    """
    try:
        # Open the Word document
        doc = Document(docx_path)
        text = ""
        
        # Extract text from each paragraph
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        return text.strip()
    
    except Exception as e:
        print(f"Error extracting text from {docx_path}: {str(e)}")
        return None

def extract_text_from_file(file_path: str, use_langchain: bool = False) -> Optional[str]:
    """
    Extract text from a file, automatically detecting the file type.
    Supports PDF (.pdf) and Word (.docx) files.
    
    Args:
        file_path (str): Path to the file
        use_langchain (bool): Whether to use LangChain loader for PDFs
        
    Returns:
        str: Extracted text from the file, or None if extraction fails
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.pdf':
        if use_langchain:
            return extract_text_from_pdf_langchain(file_path)
        else:
            return extract_text_from_pdf_pymupdf(file_path)
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)
    else:
        print(f"Unsupported file type: {file_extension}. Supported types: .pdf, .docx")
        return None

def read_resume_and_jd(resume_path: str, jd_path: str, use_langchain: bool = False) -> tuple[Optional[str], Optional[str]]:
    """
    Read two files (PDF or Word documents) and extract text from them.
    
    Args:
        resume_path (str): Path to the resume file (.pdf or .docx)
        jd_path (str): Path to the job description file (.pdf or .docx)
        use_langchain (bool): Whether to use LangChain loader for PDFs
        
    Returns:
        tuple: (resume_text, jd_text) - extracted text from both files
    """
    # Extract text from resume file
    resume = extract_text_from_file(resume_path, use_langchain)
    
    # Extract text from job description file
    jd = extract_text_from_file(jd_path, use_langchain)
    
    return resume, jd

def get_documents_from_pdf(pdf_path: str) -> List[dict]:
    """
    Get structured documents from PDF using LangChain loader.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        List[dict]: List of documents with metadata
    """
    try:
        loader = pfl(pdf_path)
        documents = loader.load()
        
        # Convert to list of dictionaries
        docs = []
        for i, doc in enumerate(documents):
            docs.append({
                'page': i + 1,
                'content': doc.page_content,
                'metadata': doc.metadata
            })
        
        return docs
    
    except Exception as e:
        print(f"Error loading documents from {pdf_path}: {str(e)}")
        return []

def main():
    """
    Main function to demonstrate usage.
    """
    # Example usage
    resume_path = "Files/res1.pdf"
    jd_path = "Files/ETL_jd.docx"
    
    # Test with PyMuPDF
    print("Testing with PyMuPDF...")
    resume, jd = read_resume_and_jd(resume_path, jd_path, use_langchain=False)
    
    if resume:
        print(f"✅ Resume extracted: {len(resume)} characters")
    if jd:
        print(f"✅ JD extracted: {len(jd)} characters")
    
    # Test with LangChain
    print("\nTesting with LangChain...")
    resume_lc, jd_lc = read_resume_and_jd(resume_path, jd_path, use_langchain=True)
    
    if resume_lc:
        print(f"✅ Resume extracted (LangChain): {len(resume_lc)} characters")
    if jd_lc:
        print(f"✅ JD extracted (LangChain): {len(jd_lc)} characters")

if __name__ == "__main__":
    main() 