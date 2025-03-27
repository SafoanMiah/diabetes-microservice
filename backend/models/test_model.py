import pickle
import pandas as pd


def test_model_output():
    # Loading the model
    with open("backend/models/linear_regression_model.pkl", "rb") as f:
        model = pickle.load(f)

    # Test dictionary
    test_data = {
        "age": 50,  # age in years
        "sex": 1,  # sex (1: male, 0: female)
        "bmi": 26.5,  # Body mass index
        "bp": 85,  # Average blood pressure
        "tc": 140,  # Total serum cholesterol
        "ldl": 80,  # Low-density lipoproteins
        "hdl": 70,  # High-density lipoproteins
        "tch": 30,  # Total cholesterol / HDL
        "ltg": 5.5,  # Log of serum triglycerides level
        "glu": 100,  # Blood sugar level
    }

    # To DF and predict
    test_df = pd.DataFrame([test_data])
    prediction = model.predict(test_df)

    # Print the prediction
    print(f"Model prediction: {prediction}")

    # Assert for output and make sure its a number, (model)
    assert isinstance(prediction[0], (int, float))


if __name__ == "__main__":
    test_model_output()
