# Resume Screening System

An AI-powered resume screening system that analyzes resumes against job descriptions and provides scoring and recommendations.

## Features

- **AI-Powered Analysis**: Uses CrewAI agents to analyze resumes and job descriptions
- **Structured Output**: Provides detailed analysis with scoring out of 10
- **Excel Integration**: Automatically saves all results to an Excel file for tracking
- **Persistent Storage**: All screening results are appended to maintain history
- **Analytics**: Provides summary statistics and score distribution

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Screening**:
   ```bash
   cd Services
   python main.py
   ```

3. **View Results**:
   - Console output shows immediate results
   - Excel file: `Files/screening_results.xlsx`
   - Markdown report: `report.md`

## Excel Integration

The system automatically saves all screening results to an Excel file that:
- ✅ Appends new results for every input
- ✅ Maintains complete history of all screenings
- ✅ Provides analytics and statistics
- ✅ Tracks candidate scores and details

### Excel File Structure:
- **Timestamp**: When screening was performed
- **Candidate_Name**: Name from resume
- **JD_Role**: Job role from description
- **Phone_Number**: Contact from resume
- **Email**: Email from resume
- **Score**: Score in X/10 format
- **Score_Numeric**: Numeric score for calculations
- **Additional_Information**: Summary and reasoning
- **Resume_File**: Source resume file
- **JD_File**: Source job description file

## Testing

### Test Excel Functionality:
```bash
cd Services
python test_excel.py
```

### View Excel Contents:
```bash
cd Services
python view_excel.py
```

## File Structure

```
Resume-Screener/
├── Services/
│   ├── main.py              # Main application with Excel integration
│   ├── task_def.py          # Task definitions
│   ├── agent_def.py         # Agent definitions
│   ├── test_excel.py        # Excel functionality test
│   └── view_excel.py        # Excel file viewer
├── Utils/
│   ├── excel_manager.py     # Excel operations
│   ├── document_reader.py   # Document processing
│   └── file_reader.py       # File reading utilities
├── Commons/
│   └── config.py            # Configuration
├── Files/
│   ├── screening_results.xlsx  # Generated Excel file
│   ├── res1.pdf             # Sample resumes
│   ├── res2.pdf
│   └── ETL_jd.docx          # Sample job description
└── requirements.txt          # Dependencies
```

## Score Categories

- **8-10**: Excellent candidates, strong match
- **7**: Good candidates, worth considering  
- **≤6**: Poor match, not recommended

## Dependencies

- `crewai`: AI agent framework
- `pandas`: Data manipulation and Excel operations
- `openpyxl`: Excel file handling
- `PyMuPDF`: PDF processing
- `python-docx`: Word document processing
- `langchain-openai`: LLM integration

For detailed Excel functionality documentation, see [README_Excel.md](README_Excel.md).
