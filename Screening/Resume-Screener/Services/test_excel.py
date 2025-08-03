import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.excel_manager import ExcelManager

def test_excel_functionality():
    """Test the Excel functionality with sample data"""
    print("🧪 Testing Excel functionality...")
    
    # Initialize Excel manager
    excel_manager = ExcelManager()
    
    # Sample crew results for testing
    sample_results = [
        """
        Name: John Doe
        JD_Role: Data Engineer
        Phone_Number: +1-555-0123
        Email: john.doe@email.com
        Score: 8/10
        Additional_Information: Strong Python skills, relevant experience in ETL pipelines, good understanding of data modeling
        """,
        """
        Name: Jane Smith
        JD_Role: Software Developer
        Phone_Number: +1-555-0456
        Email: jane.smith@email.com
        Score: 6/10
        Additional_Information: Limited experience with required technologies, needs more backend development experience
        """,
        """
        Name: Mike Johnson
        JD_Role: Data Scientist
        Phone_Number: +1-555-0789
        Email: mike.johnson@email.com
        Score: 9/10
        Additional_Information: Excellent match with all required skills, strong statistical background, relevant project experience
        """
    ]
    
    # Test file paths
    resume_files = ["Files/res1.pdf", "Files/res2.pdf", "Files/res1.pdf"]
    jd_files = ["Files/ETL_jd.docx", "Files/ETL_jd.docx", "Files/ETL_jd.docx"]
    
    # Append sample results
    for i, (result, resume_file, jd_file) in enumerate(zip(sample_results, resume_files, jd_files)):
        print(f"\n📝 Adding sample result {i+1}...")
        success = excel_manager.append_result(resume_file, jd_file, result)
        
        if success:
            print(f"✅ Sample result {i+1} added successfully")
        else:
            print(f"❌ Failed to add sample result {i+1}")
    
    # Get and display final statistics
    print("\n📊 Final Statistics:")
    stats = excel_manager.get_summary_stats()
    if isinstance(stats, dict):
        print(f"   📊 Total Candidates: {stats['total_candidates']}")
        print(f"   📊 Average Score: {stats['average_score']:.2f}" if stats['average_score'] != 'N/A' else f"   📊 Average Score: {stats['average_score']}")
        print(f"   🎯 High Scores (8-10): {stats['high_scores']}")
        print(f"   📋 Medium Scores (6-7): {stats['medium_scores']}")
        print(f"   ⚠️ Low Scores (<6): {stats['low_scores']}")
    else:
        print(f"📈 {stats}")
    
    print(f"\n📁 Excel file location: {excel_manager.excel_file_path}")
    print("✅ Excel functionality test completed!")

if __name__ == "__main__":
    test_excel_functionality() 