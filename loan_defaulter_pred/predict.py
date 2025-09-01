
import pandas as pd
from custom_utils import home_ownership_mapping, loan_grade_mapping, default_on_file_mapping

import joblib

# Load model
rf_model = joblib.load("trained_model/rf_model_loan_default_pred.pkl")


# Load encoder
loan_intent_encoder = joblib.load("trained_model/loan_intent_encoder.pkl")


# Inference
sample_input = {'person_age': 30,
                'person_income': 1000000,
                'person_home_ownership': home_ownership_mapping['RENT'],
                'person_emp_length': 6.0,
                'loan_intent': loan_intent_encoder.transform(['DEBTCONSOLIDATION'])[0],
                'loan_grade': loan_grade_mapping['B'],
                'loan_amnt': 500000,
                'loan_int_rate': 11.89,
                'loan_percent_income': 0.5,
                'cb_person_default_on_file': default_on_file_mapping['N'],
                'cb_person_cred_hist_length': 4}

sample_input_df = pd.DataFrame(sample_input, index=[0])



def make_prediction(sample_input_df):
    prediction = rf_model.predict(sample_input_df)
    label = "Likely to default" if prediction[0] == 1 else "Less likely to default"
    return label


if __name__ == "__main__":
    pred = make_prediction(sample_input_df)
    print(pred)
