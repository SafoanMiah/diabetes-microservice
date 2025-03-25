import pytest
import pickle
import numpy as np
import pandas as pd

def test_model_output():

    # Loading the model
    with open("backend/models/linear_regression_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Test dictionary
    test_data = {
        'age': 1.0,
        'sex': 1,
        'bmi': 1.0,
        'bp': 1.0,
        'tc': 1.0,
        'ldl': 1.0,
        'hdl': 1.0,
        'tch': 1.0,
        'ltg': 1.0,
        'glu': 1.0
    }
    
    # To DF
    test_df = pd.DataFrame([test_data])
    
    # Predict
    prediction = model.predict(test_df)
    
    # Print the prediction
    print(f"Model prediction: {prediction}")
    
    # Assert for output and make sure its a number, (model does give valid output)
    assert isinstance(prediction[0], (int, float))