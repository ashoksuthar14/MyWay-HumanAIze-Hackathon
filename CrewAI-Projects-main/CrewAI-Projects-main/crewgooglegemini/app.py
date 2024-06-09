# app.py
import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

st.title("CrewAI Task Execution")

# Input field for the topic
topic = st.text_input("Enter a topic:", "photosynthesis")

# Execute the CrewAI tasks
crew = Crew(agents=[news_researcher, news_writer], tasks=[research_task, write_task], process=Process.sequential)
result = crew.kickoff(inputs={'topic': topic})

# Display the results
st.write("Research Task Result:")
st.write(result[research_task])

st.write("Writing Task Result:")
st.write(result[write_task])
