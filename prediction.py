from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the model
model = joblib.load('optimized_xgboost_model.pkl')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Input data in JSON format
    df = pd.DataFrame(data)  # Convert to DataFrame
    predictions = model.predict(df)  # Make predictions
    return jsonify(predictions.tolist())  # Return predictions as JSON


if __name__ == '__main__':
    app.run(debug=True)
