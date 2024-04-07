import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Function to get BMI from height and weight
def calculate_bmi(height_cm, weight_kg):
    height_m = float(height_cm) / 100
    weight_kg = float(weight_kg)
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Function to calculate age from birth date
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Function to load data from CSV
def load_data_from_csv(filename):
    df = pd.read_csv(filename)
    return df

# Function to generate BMI distribution by gender chart
def bmi_distribution_by_gender(data):
    data['bmi'] = data.apply(lambda row: calculate_bmi(row['height'], row['weight']), axis=1)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='bmi', hue='gender', bins=20, kde=True)
    plt.title('BMI Distribution by Gender')
    plt.xlabel('BMI')
    plt.ylabel('Frequency')
    st.pyplot(plt)

# Function to generate BMI distribution by state chart
def bmi_distribution_by_state(data):
    data['bmi'] = data.apply(lambda row: calculate_bmi(row['height'], row['weight']), axis=1)
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='state', y='bmi')
    plt.title('BMI Distribution by State')
    plt.xlabel('State')
    plt.ylabel('BMI')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Function to generate BMI distribution by age chart
def bmi_distribution_by_age(data):
    data['bmi'] = data.apply(lambda row: calculate_bmi(row['height'], row['weight']), axis=1)
    data['birthDay'] = pd.to_datetime(data['birthDay'])
    data['age'] = data['birthDay'].apply(lambda x: calculate_age(x.date()))
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='age', y='bmi')
    plt.title('BMI Distribution by Age')
    plt.xlabel('Age')
    plt.ylabel('BMI')
    st.pyplot(plt)

# Main function to run the app
def main():
    st.title("BMI Project")

    # Load data from CSV
    data = load_data_from_csv("test_bmi.csv")

    # Display existing data table
    # st.subheader("Existing Data Table")
    # st.write(data)

   
    # Generate BMI distribution charts based on user selection
    st.subheader("BMI Distribution Charts")
    chart_type = st.selectbox("Select chart type:", ("By Gender", "By State", "By Age"))
    if chart_type == "By Gender":
        bmi_distribution_by_gender(data)
    elif chart_type == "By State":
        bmi_distribution_by_state(data)
    elif chart_type == "By Age":
        bmi_distribution_by_age(data)

     # Add new entry
    st.subheader("What is your BMI?")

    # Input fields for new entry
    name = st.text_input("Name")
    height = st.text_input("Height (cm)")
    weight = st.text_input("Weight (kg)")
    gender = st.selectbox("Gender", ["Male", "Female"])
    state = st.text_input("State")
    birth_date = st.date_input("Birth Date")

    # Add button to trigger new entry addition
    if st.button("What is your BMI?"):
        new_entry = pd.DataFrame({
            'first': [name],
            'height': [height],
            'weight': [weight],
            'gender': [gender],
            'state': [state],
            'birthDay': [birth_date.strftime('%Y-%m-%d')]
        })
        data = pd.concat([data, new_entry], ignore_index=True)
        st.success("New entry added successfully!")


if __name__ == "__main__":
    main()
