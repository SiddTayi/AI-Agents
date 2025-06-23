import streamlit as st
from travelAgents import guide_expert, location_expert, planner
from TravelTasks import guide_task, city_task, planner_task
from crewai import Crew, Process
from PIL import Image

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f7;
        color: #333;
    }
    .title {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 2.5em;
        color: #0056b3;
    }
    body {
        font-family: 'Helvetica', sans-serif;
    }
    .loading {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌍 Travel Adventure Planner ✈️", anchor="title")

st.markdown("""
    **Plan your next trip using AI!**
    - **Guide Expert**: Get personalized travel advice.
    - **Location Expert**: Discover top destinations.
    - **Planner**: Create a detailed itinerary.
    Enter your travel details below, and our AI-Powered travel assistant will create a customized travel plan for you.
""")

col1, col2 = st.columns(2)

with col1:
    from_city = st.text_input("From City:", "New York")
    start_date = st.date_input("Start Date:")
    budget = st.number_input("Budget:", value=1000)

with col2:
    to_city = st.text_input("To City:", "Paris")
    end_date = st.date_input("End Date:")
    travelers = st.number_input("Number of Travelers:", value=2)

preferences = st.text_input("Preferences:", "Describe how you'd like your trip to be. e.g., Food, Adventure, Relaxation, etc. 🌟")

if st.button("Generate Travel Plan"):
    if not from_city or not to_city or not start_date or not end_date or not budget or not travelers or not preferences:
        st.error("Please fill in all the fields. 🛑")
    else:
        st.spinner("Generating your travel plan...")

        guide_task = guide_task(location_expert, from_city, to_city, start_date, end_date, budget, travelers, preferences)
        loc_task = city_task(guide_expert, destination_city='NYC')
        planning_task = planner_task(planner, guide_task, loc_task)

        crew = Crew(
            tasks=[loc_task, guide_task, planning_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()

        travel_plan_text = str(result).replace("```markdown", "")

        st.subheader("Here's your travel plan:")
        st.markdown("### Here's your travel plan:", unsafe_allow_html=True)
        st.markdown(f"<pre style='white-space: pre-wrap;'>{travel_plan_text}</pre>", unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Travel Plan",
            data=travel_plan_text,
            file_name=f"travel_plan_{to_city}.md",
            mime="text/plain"
        )

st.markdown(
    """
    <footer>
    <p>✨ Wishing you amazing travels ahead! 🏖️🏔️✈️</p>
    </footer>
    """,
    unsafe_allow_html=True
)
