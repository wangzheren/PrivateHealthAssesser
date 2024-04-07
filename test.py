import csv
import random
import datetime

# Sample data structure similar to the 'columns' variable in sql_client_bmi.py
columns = {
    'id': {'type': 'SERIAL'},
    'first': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'last': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'height': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'weight': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'gender': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'state': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'birthDay': {'type': 'Date', 'constraints': ['NOT NULL']}
}

# Function to generate random data for each column
def generate_data():
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Emma', 'David']
    last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Taylor', 'Anderson']
    states = ['California', 'New York', 'Texas', 'Florida', 'Illinois']
    genders = ['Male', 'Female']

    data = {
        'id': random.randint(1, 1000),
        'first': random.choice(first_names),
        'last': random.choice(last_names),
        'height': f"{random.randint(140, 200)}",
        'weight': f"{random.randint(40, 120)}",
        'gender': random.choice(genders),
        'state': random.choice(states),
        'birthDay': (datetime.datetime.now() - datetime.timedelta(days=random.randint(18*365, 90*365))).strftime('%Y-%m-%d')
    }
    return data

# Generate CSV file with sample data
def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns.keys())
        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow(generate_data())

# Generate CSV file with 100 rows of sample data
generate_csv('test_bmi.csv', 100)
print("CSV file 'sample_data.csv' generated successfully.")
