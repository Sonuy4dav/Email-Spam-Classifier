from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    email = request.form['message']

    # Transform text
    transformed_email = vectorizer.transform([email])

    # Prediction
    prediction = model.predict(transformed_email)[0]

    if prediction == 1:
        result = "🚨 Spam Email"
    else:
        result = "✅ Not Spam"

    return render_template(
        'index.html',
        prediction_text=result,
        email=email
    )

if __name__ == '__main__':
    app.run(debug=True)