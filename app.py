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
        
        prediction = 0
        
        # Sample chart (this is just placeholder for now)
        chart = "Visualization placeholder"
        
        # Return the result page with all the data
        return render_template(
            "result.html",
            prediction=prediction,
            form_data=form_data,
            chart=chart
        )
    
    # Incase of any errors show this error.html page
    except Exception as e:
        return render_template(
            "error.html",
            error=str(e)
        )

if __name__ == '__main__':
    app.run(debug=True) # live updates