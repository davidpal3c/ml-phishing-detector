from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
from utils import classify_message

app = Flask(__name__)
CORS(app)  

model = load("phishing_detector_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Please provide a 'message' field in JSON"}), 400

    message = data["message"]
    result = classify_message(model, message)
    return jsonify({"classification": result})

if __name__ == "__main__":
    app.run(debug=True)
