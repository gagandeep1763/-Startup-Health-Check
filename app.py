from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and feature columns
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Get form values
        try:
            input_data = {
                'funding_total_usd': float(request.form["funding_total_usd"]),
                'milestones': int(request.form["milestones"]),
                'funding_rounds': int(request.form["funding_rounds"]),
                'relationships': int(request.form["relationships"])
            }

            # Create full feature vector
            input_full = {col: 0 for col in features}
            input_full.update(input_data)
            input_df = pd.DataFrame([input_full])

            # Make prediction
            pred = model.predict(input_df)[0]
            prediction = "✅ Startup will be Success" if pred == 1 else "❌ Startup is likely to be a Failure"

        except Exception as e:
            prediction = f"⚠️ Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
