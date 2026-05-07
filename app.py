from flask import Flask, render_template, request
import joblib
from feature_extraction import extract_features
from utils.rules import detect_attack_type

# CREATE APP
app = Flask(__name__)

# LOAD MODEL
model = joblib.load("model.pkl")


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# PREDICTION ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    # STEP 1: RULE-BASED DETECTION
    rule_result = detect_attack_type(url)

    if rule_result:
        result = f"{rule_result} Attack Detected"

    else:
        # STEP 2: ML MODEL CHECK
        features = extract_features(url)
        prediction = model.predict([features])[0]

        if prediction == 1:
            result = "Malicious URL (Unknown Type)"
        else:
            result = "Safe URL"

    return render_template('index.html', prediction=result)


# RUN APP
if __name__ == '__main__':
    app.run(debug=True)