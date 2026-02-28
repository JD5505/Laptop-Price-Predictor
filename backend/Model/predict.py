import pandas as pd
import joblib


model = joblib.load('Model/model.pkl')

MODEL_VERSION = '1.0.0'

def user_input(input_dict : dict):
    input_df = pd.DataFrame([input_dict])

    output = model.predict(input_df)[0]

    return output