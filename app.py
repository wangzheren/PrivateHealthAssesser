import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from SQL_Client_BMI import add_entry,create_connection, create_table


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
    st.text("This graph shows the males' distribution of BMI (Body Mass Index) is generally larger than females.")

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
    st.text("This graph shows the Illinios' distribution of BMI (Body Mass Index) is the highest and Florida the lowest compared to all states.")

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
    st.text("This graph shows BMI ranges for all ages and there are no clear patterns.")

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

    if height != '' and weight != '':
        # Calculate BMI for the new entry
        new_bmi = calculate_bmi(height, weight)

        # Determine BMI category
        bmi_category = ""
        if new_bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= new_bmi < 25:
            bmi_category = "Normal weight"
        elif 25 <= new_bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        if bmi_category == "Underweight":
            color = "orange"
        elif bmi_category == "Normal weight":
            color = "green"
        elif bmi_category == "Overweight":
            color = "yellow"
        else:
            color = "red"

        st.write(f"Your BMI is <span style='color:{color}; font-size:20px;'>{new_bmi:.2f}</span>, which is considered <span style='color:{color}; font-size:20px;'>{bmi_category}</span>.", unsafe_allow_html=True)

        # Add button to trigger new entry addition
        if st.button("Add Entry"):
            new_entry = pd.DataFrame({
                'Name': [name],
                'Height (cm)': [height],
                'Weight (kg)': [weight],
                'Gender': [gender],
                'State': [state],
                'Birth Date': [birth_date.strftime('%Y-%m-%d')],
                'BMI': [new_bmi]
            })
            columns = {
                'name': {'type': 'VARCHAR(255)'},
                'height_cm': {'type': 'FLOAT'},
                'weight_kg': {'type': 'FLOAT'},
                'gender': {'type': 'VARCHAR(10)'},
                'state': {'type': 'VARCHAR(50)'},
                'birth_date': {'type': 'DATE'},
                'bmi': {'type': 'FLOAT'}
}
            create_table('new_data_table', columns)
            add_entry('new_data_table', new_entry)
            # data = pd.concat([data, new_entry], ignore_index=True)
            
            st.success("New entry added successfully!")
            # # Call count_entries function to get the total number of entries
            # total_entries = count_entries('new_data_table')

            # # Display the total number of entries
            # st.write(f"Total entries in the database: {total_entries}")

            # new_entry_id = 1  # Replace 123 with the actual ID of the new entry
            # entry = get_entry_by_id('new_data_table', new_entry_id)
            # if entry:
            #     st.write("New entry in database:", entry)
            # else:
            #     st.write("Failed to retrieve new entry from database.")
    else:
        st.warning("Please enter valid values for height and weight.")

if __name__ == "__main__":
    main()
