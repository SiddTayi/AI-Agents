from crewai import Task

def resume_task(agent, resume):
    return Task(
        agent = agent,
        description =f"""
                ---------------
                Resume: {resume}
                ---------------
                GUIDELINES:
                    1. You are an expert in analyzing a resume and extracting important information such as Education, Experience, Projects, Tech Stack, skills, etc. 
                    2. You should be extremely careful while extracting information since it contains experience which has the most weightage.
                    3. Follow the JSON Schema and fill the extracted information in their respective fields. 
                    4. A candidate could have experience working in different companies. Each of these companies are to be treated as a list in the JSON Schema. Create a new list for every experience.
                    5. A candidate would have gone to different schools. You are supposed to create a new list for every school/education.
                    6. "additional_information" should contain any extra information that was seen/observed in the resume that has to be highlighted. It can be anything.  
                """,
        expected_output = """
                    JSON SCHEMA:
                    {
                        "Name" : "",
                        "Phone_Number" : "",
                        "Email": "",
                        "Experience": [
                            {
                                "Company": "",
                                "Role": "",
                                "Responsibilities": "",
                                "Tech_Stack": "A list of technologies and skills seperated by a comma",
                                "Skills": "A list of skills seperated by a comma",
                                "Experience_in_years": "A numeric value containing the duration of the stay in the company."
                            },
                        ],
                        "Projects": [
                            {
                                "Title": "",
                                "Description": "",
                                "Skills": "",
                            },
                        ],
                        "Education": [
                            {
                                "School_name": "",
                                "Start_Date": "MM-YYYY",
                                "End_Date": "MM-YYYY",
                                "Major": "",
                                "Degree": ""
                            },
                        ],
                        "additional_information": "",
                        "confidence": "out of 100"
                    }
        """
    )

def hiring_task(agent, jd, resume, context):
    return Task(
        agent = agent,
        description = f"""
            ---------------
                JD: {jd}
            ---------------
            Resume: {resume}
            ---------------

            1. Analyze the resume with the JD and come up with a score. 
            2. Carefully identify and compare key skills that are needed to shortlist a candidate. 
            3. Use industry standard practices to consider a candidate with no bias and discrimination.  
            4. The scoring system is out of 10. 10 being the highest and 0 being the lowest. 
            5. The score :
                8-10: highest relevancy - good match with all the skills aligning with the JD. 
                7: can be considered
                <= 6: Do not consider.      
            6. Extract the candidate's name, phone number, and email from the resume if available.
            7. Provide the job role/title from the JD.
            8. Format your response as a structured table with clear headers and values.
        """,
        expected_output = """
            Create a structured table with the following information. Format it clearly with headers and values separated by colons or pipes.
            
            REQUIRED FIELDS:
            Name: [Candidate's name from resume]
            JD_Role: [Job role/title from JD]
            Phone_Number: [Phone number from resume if available]
            Email: [Email from resume if available]
            Score: [X/10 format]
            Additional_Information: [Brief summary of key strengths/weaknesses and reasoning for score]
            
            Example format:
            | Name | JD_Role | Phone_Number | Email | Score | Additional_Information |
            |------|---------|--------------|-------|-------|----------------------|
            | John Doe | Data Engineer | +1-555-0123 | john@email.com | 8/10 | Strong Python skills, relevant experience in ETL pipelines |
            
            OR use this format:
            Name: John Doe
            JD_Role: Data Engineer
            Phone_Number: +1-555-0123
            Email: john@email.com
            Score: 8/10
            Additional_Information: Strong Python skills, relevant experience in ETL pipelines
        """,
        output_file="report.md",
        context = context
    )