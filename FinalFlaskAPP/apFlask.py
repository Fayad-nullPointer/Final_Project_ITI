from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model\Model2.pkl')

# Render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Handle the form submission and predict
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    form_data = request.form.to_dict()
    
    # Prepare the data for prediction
    new_data = pd.DataFrame({
        'age': [form_data['age']],
        'sex': [form_data['gender']],
        'cp': [form_data['chestPain']],
        'trtbps': [form_data['restingBP']],
        'chol': [form_data['cholesterol']],
        'fbs': [form_data['fastingBS']],
        'restecg': [form_data['restingECG']],
        'thalachh': [form_data['maxHR']],
        'exng': [form_data['exerciseInducedAngina']],
        'oldpeak': [form_data['previousPeak']]
    })
    

    # Make prediction
    prediction = model.predict(new_data)
    
    # Decode the prediction
    prediction_label = 'You are in dengerous !!' if prediction[0]== 1 else 'Safe'
    # Render the result page with prediction
    return render_template("index.html",prediction=prediction_label)

if __name__ == '__main__':
    app.run(debug=True)
