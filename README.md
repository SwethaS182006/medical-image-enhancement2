# EHR Data Visualization for Inpatient Readmission Analysis

Hi! This project is all about exploring a simulated Electronic Health Record (EHR) dataset to understand patterns behind inpatient readmissions. I used Python to clean the data, encode categorical variables, and create visualizations that highlight key relationships in the dataset.

## What This Project Does

- It loads a CSV file with patient data, including age, gender, diagnosis codes, lab results, and readmission status.
- It cleans and transforms the data so it's ready for analysis.
- It creates four visualizations to help us understand how different factors relate to readmission risk:
  - A correlation heatmap
  - An age distribution plot
  - A scatter plot of risk score vs. length of stay
  - A box plot comparing procedures between readmitted and non-readmitted patients

## Dataset Used

**File:** `Simulated_Inpatient_Readmission_Dataset.csv`  
This dataset includes:
- Patient demographics (Age, Gender)
- Clinical metrics (Risk Score, Length of Stay, Number of Procedures)
- Diagnosis codes and lab abnormalities
- Readmission status within 30 days

## How the Code Works

1. I start by loading the dataset using pandas.
2. Then I clean up missing values and convert categorical columns like gender and readmission status into numeric format.
3. I use one-hot encoding to handle diagnosis codes and lab abnormalities.
4. I select the numeric columns and create a 2x2 grid of plots using matplotlib and seaborn.
5. Finally, I display all the plots together so we can visually explore the data.

## How to Run It

1. Make sure you have Python 3.7 or higher installed.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn
python ehr_visualization.py
