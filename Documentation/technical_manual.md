# BMI Project Technical Manual

Welcome to the BMI Project! This manual provides detailed instructions for deploying the application, utilizing its features, and special instructions for grading purposes.

## Deployment

1. **Clone the Repository**: Begin by cloning the BMI Project repository to your local machine:

   ```bash
   git clone https://github.gatech.edu/zwang939/6440Project.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
bash

```bash
cd bmi-streamlit
pip install -r requirements.txt
```

3. **Database Setup**: Ensure PostgreSQL is installed and running on your system. Modify the database connection settings in the code to match your PostgreSQL setup.

4. **Run the Application**: Launch the BMI Project app using Streamlit:

```bash
streamlit run app.py
```

5. **Access the Application**: Open your web browser and navigate to the URL displayed in the terminal where Streamlit is running (typically http://localhost:8501).

6. **Streamlit Platform Deployment**:
   * Push your code to GitHub repository.
   * Sign up or log in to Streamlit Sharing.
   * Click 'New app', then enter your repo, branch, and path to your app.
   * Click 'Deploy', and Streamlit will do the rest.