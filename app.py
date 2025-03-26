from flask import Flask, render_template, request, flash, redirect
import pickle
import json
import pandas as pd

app = Flask(__name__)

# Loading in model
with open("backend/models/linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)
    print("Linear Regression Model loaded successfully")

with open("templates/chart/chart.json", "r") as f:
    diabetes_chart = json.load(f)

# Main page
@app.route("/") 
def index():
    return render_template("index.html")

# This adds a POST (send to api) prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract all the information from the form
        form_data = {
            'age': float(request.form["age"]),
            'sex': int(request.form["sex"]),
            'bmi': float(request.form["bmi"]),
            'bp': float(request.form["bp"]),
            'tc': float(request.form["tc"]),
            'ldl': float(request.form["ldl"]),
            'hdl': float(request.form["hdl"]),
            'tch': float(request.form["tch"]),
            'ltg': float(request.form["ltg"]),
            'glu': float(request.form["glu"])
        }

        # Get prediction
        data_features = pd.DataFrame([form_data])
        prediction = model.predict(data_features)
        prediction = round(prediction[0], 1) # 1d.p same as dataset
        
        # Sample chart (this is just placeholder for now)
        chart = "Visualization placeholder"
        
        # Return the result page with all the data
        return render_template(
            "result.html",
            prediction=prediction,
            form_data=form_data,
            chart=diabetes_chart
        )
    
    # Error handling, return page with an error message
    except Exception as e:
        return render_template(
            "error.html",
            error=str(e)
        )


if __name__ == '__main__':
    app.run(debug=True) # live updates