import pandas as pd
import os
from datetime import datetime
import json
import re

class ExcelManager:
    def __init__(self, excel_file_path="Files/screening_results.xlsx"):
        # Get the absolute path to the Files directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        self.excel_file_path = os.path.join(project_root, excel_file_path)
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        """Create the Excel file with headers if it doesn't exist"""
        if not os.path.exists(self.excel_file_path):
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.excel_file_path), exist_ok=True)
            
            # Create initial DataFrame with headers
            initial_data = {
                'Timestamp': [],
                'Candidate_Name': [],
                'JD_Role': [],
                'Phone_Number': [],
                'Email': [],
                'Score': [],
                'Score_Numeric': [],
                'Additional_Information': [],
                'Resume_File': [],
                'JD_File': []
            }
            
            df = pd.DataFrame(initial_data)
            df.to_excel(self.excel_file_path, index=False)
            print(f"✅ Created new Excel file: {self.excel_file_path}")
    
    def extract_score_numeric(self, score_text):
        """Extract numeric score from text like '8/10' or '8 out of 10'"""
        if not score_text:
            return None
        
        # Try to extract number from various formats
        patterns = [
            r'(\d+)/10',  # 8/10
            r'(\d+)\s*out\s*of\s*10',  # 8 out of 10
            r'(\d+)',  # just a number
        ]
        
        for pattern in patterns:
            match = re.search(pattern, str(score_text), re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        return None
    
    def parse_crew_result(self, result_text):
        """Parse the crew result to extract structured data"""
        try:
            # Handle CrewOutput objects
            if hasattr(result_text, 'raw'):
                result_text = result_text.raw
            elif hasattr(result_text, '__str__'):
                result_text = str(result_text)
            else:
                result_text = str(result_text)
            
            # Try to extract JSON-like structure from the result
            # Look for patterns that might contain the structured data
            lines = result_text.split('\n')
            data = {
                'Name': '',
                'JD_Role': '',
                'Phone_Number': '',
                'Email': '',
                'Score': '',
                'Additional_Information': ''
            }
            
            for line in lines:
                line = line.strip()
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().replace('|', '').strip()
                    value = value.strip()
                    
                    if key.lower() in ['name', 'candidate name']:
                        data['Name'] = value
                    elif key.lower() in ['jd role', 'role', 'job role']:
                        data['JD_Role'] = value
                    elif key.lower() in ['phone', 'phone number', 'phone_number']:
                        data['Phone_Number'] = value
                    elif key.lower() in ['email', 'e-mail']:
                        data['Email'] = value
                    elif key.lower() in ['score', 'rating']:
                        data['Score'] = value
                    elif key.lower() in ['additional information', 'additional_information', 'notes']:
                        data['Additional_Information'] = value
            
            return data
        except Exception as e:
            print(f"⚠️ Warning: Could not parse result text: {e}")
            return {
                'Name': 'Unknown',
                'JD_Role': 'Unknown',
                'Phone_Number': '',
                'Email': '',
                'Score': '0/10',
                'Additional_Information': str(result_text)[:200] + '...' if len(str(result_text)) > 200 else str(result_text)
            }
    
    def append_result(self, resume_file, jd_file, crew_result):
        """Append a new screening result to the Excel file"""
        try:
            # Parse the crew result
            parsed_data = self.parse_crew_result(crew_result)
            
            # Extract numeric score
            score_numeric = self.extract_score_numeric(parsed_data['Score'])
            
            # Prepare new row data
            new_row = {
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Candidate_Name': parsed_data['Name'],
                'JD_Role': parsed_data['JD_Role'],
                'Phone_Number': parsed_data['Phone_Number'],
                'Email': parsed_data['Email'],
                'Score': parsed_data['Score'],
                'Score_Numeric': score_numeric,
                'Additional_Information': parsed_data['Additional_Information'],
                'Resume_File': os.path.basename(resume_file),
                'JD_File': os.path.basename(jd_file)
            }
            
            # Read existing data
            try:
                df = pd.read_excel(self.excel_file_path)
            except FileNotFoundError:
                # If file doesn't exist, create new DataFrame
                df = pd.DataFrame()
            
            # Append new row
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
            # Save to Excel
            df.to_excel(self.excel_file_path, index=False)
            
            print(f"✅ Results appended to Excel file: {self.excel_file_path}")
            print(f"📊 Total records in file: {len(df)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error appending to Excel: {e}")
            return False
    
    def get_summary_stats(self):
        """Get summary statistics from the Excel file"""
        try:
            df = pd.read_excel(self.excel_file_path)
            
            if len(df) == 0:
                return "No data available"
            
            stats = {
                'total_candidates': len(df),
                'average_score': df['Score_Numeric'].mean() if 'Score_Numeric' in df.columns else 'N/A',
                'high_scores': len(df[df['Score_Numeric'] >= 8]) if 'Score_Numeric' in df.columns else 'N/A',
                'medium_scores': len(df[(df['Score_Numeric'] >= 6) & (df['Score_Numeric'] < 8)]) if 'Score_Numeric' in df.columns else 'N/A',
                'low_scores': len(df[df['Score_Numeric'] < 6]) if 'Score_Numeric' in df.columns else 'N/A'
            }
            
            return stats
            
        except Exception as e:
            print(f"❌ Error getting summary stats: {e}")
            return "Error retrieving statistics" 