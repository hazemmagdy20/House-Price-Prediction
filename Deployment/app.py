from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read inputs from form
    bedroom = float(request.form['bedroom'])
    space = float(request.form['space'])
    room = float(request.form['room'])
    lot = float(request.form['lot'])
    tax = float(request.form['tax'])
    bathroom = float(request.form['bathroom'])
    garage = float(request.form['garage'])  
    condition = float(request.form['condition'])   # Do not scale this one

    # Put features into correct order
    continuous_features = np.array([[bedroom, space, room, lot, tax, bathroom]])
    
    scaled_continuous = scaler.transform(continuous_features)  # Scale only numeric features

    # Combine scaled continuous features with garage
    final_features = np.concatenate([scaled_continuous, np.array([[garage, condition]])], axis=1)

    prediction = model.predict(final_features)
    pred_value = float(prediction[0])  # Convert NumPy type to Python float
    return render_template('index.html', prediction_text=f'Predicted Price: {pred_value:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)

