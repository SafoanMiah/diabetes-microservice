from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Main page
@app.route("/") 
def index():
    return render_template("index.html")


#### TEMPORARY return in place of model prediction
# This adds a POST (send to api) prediction endpoint
# For now it returns a dummy reponse while ML model is made
@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    
    # Temporary dummy reponse
    return jsonify({
        "success": True,
        "prediction": 0,  # 0 for low risk, 1 for high risk
        "message": "API is working. Model integration coming soon.",
        "input_data": { # extract input data
            "age": data['age'],
            "sex": data['sex'],
            "bmi": data['bmi'],
            "bp": data['bp'],
            "tc": data['tc'],
            "ldl": data['ldl'],
            "hdl": data['hdl'],
            "tch": data['tch'],
            "ltg": data['ltg'],
            "glu": data['glu']
        }
    })


# GET endpoint that gives sample data for visualization, a small dataset to be specific
@app.route("/api/data", methods=["GET"])
def get_data():
    sample_data = {
        "data": [
            {"age": 45, "bmi": 22.5, "glu": 5.2, "target": 0},
            {"age": 55, "bmi": 32.1, "glu": 7.8, "target": 1},
            {"age": 35, "bmi": 24.3, "glu": 4.9, "target": 0}
        ]
    }
    
    return jsonify(sample_data)



if __name__ == '__main__':
    app.run()