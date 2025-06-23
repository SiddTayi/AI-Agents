from crewai import Task
import os

def guide_task(agent, from_city, destination_city, start_date, end_date, budget, travelers, preferences):
    return Task(
        description=f"""This task involves a comprehensive data collection process to provide the traveler with essential information about their trip.
    Given the information, formulate a plan with your research and recommendations. 

    Traveling from: {from_city}
    Destination: {destination_city}
    Start date: {start_date}
    End date: {end_date}
    Budget: {budget}
    Travelers: {travelers}
    Preferences: {preferences}

    Based on the user's preference, formulate a plan with your research and recommendations. This preference section is what the traveler wants to do and see in their trip. 
    The plan should include:
    - Detailed itinerary for each day of the trip
    - Accommodation recommendations
    - Transportation recommendations
    - Food recommendations
    - Local attractions and activities
    - Budget breakdown
    - Tips and advice for the trip
    - Emergency contacts and important information
    - Packing list
    """,
        expected_output="A detailed travel plan with all the information mentioned above in a markdown format.",
        agent=agent,
        output_file="outputs/guide_plan.md"
)


def city_task(agent, destination_city):
    return Task(
        description=f"""This task involves collecting data about the city {destination_city} to provide the traveler with essential information about their trip.
    Given the information, formulate a plan with your research and recommendations. Mention free stuff to do in the city and anything that's fun and can be done with less budget. 
    City: {destination_city}
    """,
        expected_output="A detailed city guide in markdown format.",
        agent=agent,
        output_file="outputs/city_guide.md"
)


def planner_task(agent, guide_task, city_task):
    return Task(
        description=f"""This task involves creating a detailed markdown file with the itinerary for the trip. Create flowchats and budget reports that are easy to understand.""",
        expected_output="A detailed itinerary in markdown format",
        agent=agent,
        context=[guide_task, city_task],
        output_file="outputs/itinerary.md"
)
