from flask import Flask, render_template, request
import joblib
import os
import pandas as pd

app = Flask(__name__)

# Get the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the saved model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "heart_disease_model.pkl"
)

# Load the trained model
model = joblib.load(MODEL_PATH)

print("Model loaded successfully!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    age = float(request.form["age"])
    sex = request.form["sex"]
    chest_pain = request.form["chest_pain"]
    resting_bp = float(request.form["resting_bp"])
    cholesterol = float(request.form["cholesterol"])
    fasting_bs = int(request.form["fasting_bs"])
    resting_ecg = request.form["resting_ecg"]
    max_hr = float(request.form["max_hr"])
    exercise_angina = request.form["exercise_angina"]
    oldpeak = float(request.form["oldpeak"])
    st_slope = request.form["st_slope"]

    # Create the 20 features expected by the model
    input_data = pd.DataFrame([{
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        "Sex_F": 1 if sex == "F" else 0,
        "Sex_M": 1 if sex == "M" else 0,

        "ChestPainType_ASY": 1 if chest_pain == "ASY" else 0,
        "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
        "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,
        "ChestPainType_TA": 1 if chest_pain == "TA" else 0,

        "RestingECG_LVH": 1 if resting_ecg == "LVH" else 0,
        "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
        "RestingECG_ST": 1 if resting_ecg == "ST" else 0,

        "ExerciseAngina_N": 1 if exercise_angina == "N" else 0,
        "ExerciseAngina_Y": 1 if exercise_angina == "Y" else 0,

        "ST_Slope_Down": 1 if st_slope == "Down" else 0,
        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "ST_Slope_Up": 1 if st_slope == "Up" else 0
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probability of class 1
    probability = model.predict_proba(input_data)[0][1]

    # Convert prediction into readable text
    if prediction == 1:
        result = "Higher heart attack risk"
    else:
        result = "Lower heart attack risk"

    return render_template(
        "result.html",
        result=result,
        probability=round(probability * 100, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
