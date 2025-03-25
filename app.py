from flask import Flask, render_template, request, flash, redirect
import pandas as pd

app = Flask(__name__)

# Main page
@app.route("/") 
def index():
    return render_template("index.html")

#### TEMPORARY return in place of model prediction
# This adds a POST (send to api) prediction endpoint
# For now it returns a dummy reponse while ML model is made
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
        
        # Return a dummy prediction (0 = low risk, 1 = high risk)
        prediction = 0
        
        # Sample chart (this is just placeholder for now)
        chart = "Visualization placeholder"
        
        # Return the result template with all the data
        return render_template(
            "result.html",
            prediction=prediction,
            form_data=form_data,
            chart=chart
        )
    
    # Error handling, return a 404 page like tab with an error message
    except Exception as e:
        print("Error:", str(e))
        return render_template(
            "error.html",
            error=str(e)
        )


# GET endpoint that gives sample data for visualization, a small dataset to be specific
@app.route("/api/data", methods=["GET"])
def get_data():
    data = [
        {"age": 45, "bmi": 22.5, "glu": 5.2, "target": 0},
        {"age": 55, "bmi": 32.1, "glu": 7.8, "target": 1},
        {"age": 35, "bmi": 24.3, "glu": 4.9, "target": 0}
    ]
    
    return {"data": data}


if __name__ == '__main__':
    app.run(debug=True) # for live updates