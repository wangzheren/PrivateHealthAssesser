# BMI Project Research

## Academic Research
Our project required a deep dive into the academic research surrounding the implications of Body Mass Index (BMI) on public health. We extensively reviewed literature on the epidemiology of obesity, including several peerreviewed articles and meta-analyses that explore the correlations between BMI and various chronic diseases such as type 2 diabetes, heart disease, and certain cancers. Particularly enlightening was the research indicating demographic disparities in BMI distributions, which informed our decision to include demographic factors such as age, gender, and location in our data analysis. However, a significant gap was noticed in longitudinal studies concerning the impact of urbanization on BMI changes over time, which limited our ability to model these effects accurately in our tool. This gap underscored the need for more comprehensive data collection and analysis methodologies in future public health research.

## Technical Research
The initial stages of our project involved exploring the potential of integrating the Fast Healthcare Interoperability Resources (FHIR) standard for accessing and processing BMI data. We thoroughly investigated the FHIR specification, examining its structure and potential use cases for healthcare data management. However, we encountered significant challenges in aligning FHIR's capabilities with our specific requirements for real-time BMI data analysis. The lack of standardized procedures for our particular use case and complexities in implementation led us to decide against using FHIR. Instead, we opted for a more direct approach using custom Python scripts and a MySQL database to manage data interactions. This shift not only simplified our development process but also provided us with greater control over data handling, ensuring faster response times and more flexible data manipulation capabilities within our application.

## Other work
During the course of the BMI Project development, several research efforts were conducted to inform decision-making and enhance project outcomes. The research activities undertaken include:

1. Leveraging Lab 4 Homework Thought Process
The team revisited the thought process and methodologies employed during Lab 4 homework assignments. This involved analyzing previous solutions, identifying effective problem-solving strategies, and exploring potential application to the BMI Project. Insights gained from this research aided in conceptualizing and structuring various components of the application.

2. Exploring SmartOnFhir API Integration
Investigation was carried out into the SmartOnFhir API to evaluate its suitability for integration with the BMI Project. The team explored the functionality, documentation, and capabilities of the API to determine its compatibility with the project requirements. Although the API offered promising features, it was ultimately deemed unnecessary for the scope of the BMI Project.

3. Evaluating Tech Tools for Project Implementation
Research was conducted to identify the most appropriate technology tools and frameworks for implementing the BMI Project. This involved assessing various options based on factors such as ease of use, scalability, community support, and alignment with project objectives. After thorough evaluation, Streamlit was selected as the primary framework for developing the BMI Project due to its simplicity, versatility, and suitability for data visualization applications.

4. Decision to Utilize Streamlit
Following extensive research and deliberation, the decision was made to utilize Streamlit as the core framework for developing the BMI Project. Streamlit was chosen for its intuitive interface, rapid prototyping capabilities, seamless integration with data analysis libraries such as pandas and matplotlib, and robust community support. This choice allowed the team to streamline development efforts, accelerate the implementation process, and deliver a user-friendly application tailored to the project requirements.

