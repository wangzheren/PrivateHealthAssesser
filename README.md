# BMI Project

This Streamlit application allows you to analyze BMI (Body Mass Index) distribution based on different factors such as gender, state, and age. Additionally, you can input your own data to calculate your BMI and see where you fall within the BMI categories.

## Installation

Before running the application, make sure you have Python installed on your system. You can install the required packages using pip:

```bash
pip install streamlit pandas matplotlib seaborn
```

# Usage

To run the BMI Project app, execute the following command in your terminal:

```bash
streamlit run app.py
```

# Functionality

## BMI Distribution Charts

You can choose from three different types of charts to visualize BMI distribution:

* By Gender: Shows the distribution of BMI across genders.
* By State: Displays the distribution of BMI across different states.
* By Age: Visualizes the relationship between age and BMI.

## Adding New Entry

You can input your own data to calculate BMI and add it to the existing dataset:

* Enter your name, height, weight, gender, state, and birth date.
* Click on "Add Entry" to include your data in the dataset.
* Your BMI and corresponding category will be displayed.

# Understanding BMI Categories
* Underweight: BMI less than 18.5
* Normal weight: BMI between 18.5 and 24.9
* Overweight: BMI between 25 and 29.9
* Obese: BMI 30 or greater

# Data Source

The data used in this application is simulated for demonstration purposes and is initially generated programmatically using Python. Each record includes information such as name, height, weight, gender, state, and birth date. While the structure and format of the data closely resemble real-world scenarios, it should be noted that the data is purely fictional and does not represent actual individuals.

Additionally, as users interact with the application and add new entries, the data source expands to include these real user inputs. New entries submitted by users are stored in a PostgreSQL database, gradually enriching the dataset with actual user data. This hybrid approach allows the application to provide both simulated data for demonstration purposes and real user-generated data for practical analysis.

# Note

This application provides BMI calculations for informational purposes only. It's always recommended to consult a healthcare professional for personalized advice regarding health and fitness.