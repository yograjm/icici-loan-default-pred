import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/credit_risk_dataset.csv")


# Handle missing values
df['loan_int_rate'] = df['loan_int_rate'].fillna(df['loan_int_rate'].mean())
df['person_emp_length'] = df['person_emp_length'].fillna(df['person_emp_length'].mean())


# Handle categorical columns
from custom_utils import home_ownership_mapping, loan_grade_mapping, default_on_file_mapping

df['person_home_ownership'] = df['person_home_ownership'].map(home_ownership_mapping)
df['loan_grade'] = df['loan_grade'].map(loan_grade_mapping)
df['cb_person_default_on_file'] = df['cb_person_default_on_file'].map(default_on_file_mapping)

# Label Encoder
from sklearn.preprocessing import LabelEncoder

loan_intent_encoder = LabelEncoder()

loan_intent_encoder.fit(df['loan_intent'])

df['loan_intent'] = loan_intent_encoder.transform(df['loan_intent'])


from sklearn.model_selection import train_test_split

# Fetures
X = df.drop('loan_status', axis=1)
# Target
y = df['loan_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

