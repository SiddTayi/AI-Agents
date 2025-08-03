# Excel Integration for Resume Screening

This document describes the Excel functionality that has been added to the Resume Screening system.

## Overview

The system now automatically saves all screening results to an Excel file (`Files/screening_results.xlsx`) that keeps appending new results for every input. This provides a persistent record of all candidates screened and their scores.

## Features

### 1. Automatic Excel File Creation
- Creates `Files/screening_results.xlsx` automatically on first run
- Includes proper headers and column structure
- Handles file creation and directory setup

### 2. Data Structure
The Excel file contains the following columns:
- **Timestamp**: When the screening was performed
- **Candidate_Name**: Name extracted from resume
- **JD_Role**: Job role from the job description
- **Phone_Number**: Phone number from resume
- **Email**: Email address from resume
- **Score**: Score in X/10 format
- **Score_Numeric**: Numeric score for calculations
- **Additional_Information**: Summary of strengths/weaknesses
- **Resume_File**: Name of the resume file processed
- **JD_File**: Name of the job description file processed

### 3. Automatic Appending
- Each new screening result is automatically appended to the Excel file
- No data loss - all results are preserved
- Maintains chronological order with timestamps

### 4. Statistics and Analytics
- Provides summary statistics after each screening
- Shows total candidates, average scores, and score distribution
- Helps track screening effectiveness over time

## Usage

### Running the Main Application
```bash
cd Resume-Screener/Services
python main.py
```

The system will:
1. Process the resume and job description
2. Generate screening results
3. Automatically save results to Excel
4. Display summary statistics

### Testing Excel Functionality
```bash
cd Resume-Screener/Services
python test_excel.py
```

This will add sample data to test the Excel functionality.

## File Structure

```
Resume-Screener/
├── Services/
│   ├── main.py              # Updated with Excel integration
│   ├── task_def.py          # Updated task definitions
│   └── test_excel.py        # Test script for Excel functionality
├── Utils/
│   ├── excel_manager.py     # New Excel management utility
│   └── document_reader.py   # Existing document reader
├── Commons/
│   └── config.py            # Configuration with file paths
├── Files/
│   ├── screening_results.xlsx  # Generated Excel file
│   ├── res1.pdf             # Resume files
│   ├── res2.pdf
│   └── ETL_jd.docx          # Job description
└── requirements.txt          # Updated with Excel dependencies
```

## Dependencies Added

- `pandas==2.1.4`: For data manipulation and Excel operations
- `openpyxl==3.1.2`: For Excel file reading/writing

## Excel Manager Class

The `ExcelManager` class provides the following methods:

### `__init__(excel_file_path)`
- Initializes the Excel manager
- Creates the Excel file if it doesn't exist

### `append_result(resume_file, jd_file, crew_result)`
- Parses crew results to extract structured data
- Appends new row to Excel file
- Returns success/failure status

### `get_summary_stats()`
- Calculates and returns summary statistics
- Includes total candidates, average scores, score distribution

### `parse_crew_result(result_text)`
- Extracts structured data from crew output
- Handles various output formats
- Provides fallback for parsing errors

## Score Categories

- **High Scores (8-10)**: Excellent candidates, strong match
- **Medium Scores (6-7)**: Good candidates, worth considering
- **Low Scores (<6)**: Poor match, not recommended

## Error Handling

- Graceful handling of parsing errors
- Fallback data when structured parsing fails
- File creation and directory handling
- Comprehensive error logging

## Benefits

1. **Persistent Record**: All screening results are saved permanently
2. **Analytics**: Track screening effectiveness over time
3. **Audit Trail**: Complete history of all candidates screened
4. **Easy Export**: Excel format allows easy sharing and analysis
5. **No Data Loss**: All results are preserved and appended

## Future Enhancements

- Filtering and sorting capabilities
- Advanced analytics and reporting
- Integration with other HR systems
- Automated email notifications
- Dashboard for visualization 