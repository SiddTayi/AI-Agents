import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd

def view_excel_contents():
    """View the contents of the Excel file"""
    excel_file = "Files/screening_results.xlsx"
    
    try:
        df = pd.read_excel(excel_file)
        print("📊 Excel File Contents:")
        print("=" * 80)
        print(df.to_string(index=False))
        print("=" * 80)
        print(f"\n📈 Summary:")
        print(f"   Total Records: {len(df)}")
        print(f"   Columns: {list(df.columns)}")
        
        if 'Score_Numeric' in df.columns:
            print(f"   Average Score: {df['Score_Numeric'].mean():.2f}")
            print(f"   Score Range: {df['Score_Numeric'].min()} - {df['Score_Numeric'].max()}")
        
    except FileNotFoundError:
        print(f"❌ Excel file not found: {excel_file}")
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")

if __name__ == "__main__":
    view_excel_contents() 