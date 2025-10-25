import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Simulated_Inpatient_Readmission_Dataset.csv")

df['Diagnosis_Code'] = df['Diagnosis_Code'].replace(['None', ''], np.nan)
df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})
df['Readmission_Within_30_Days'] = df['Readmission_Within_30_Days'].map({'Yes': 1, 'No': 0})
df = pd.get_dummies(df, columns=['Diagnosis_Code', 'Lab_Abnormalities'], dummy_na=True)

numeric_df = df.select_dtypes(include=[np.number])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("EHR Data Visualizations", fontsize=16)

sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=axes[0, 0])
axes[0, 0].set_title("Correlation Heatmap")

sns.histplot(df['Age'], bins=10, kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Age Distribution")
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_ylabel("Count")

sns.scatterplot(x='Length_of_Stay', y='Risk_Score', hue='Readmission_Within_30_Days', data=df, ax=axes[1, 0])
axes[1, 0].set_title("Risk Score vs Length of Stay")
axes[1, 0].set_xlabel("Length of Stay")
axes[1, 0].set_ylabel("Risk Score")

sns.boxplot(x='Readmission_Within_30_Days', y='Number_of_Procedures', data=df, ax=axes[1, 1])
axes[1, 1].set_title("Procedures vs Readmission")
axes[1, 1].set_xlabel("Readmission (0 = No, 1 = Yes)")
axes[1, 1].set_ylabel("Number of Procedures")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()