from flask import Flask, render_template, request
import joblib  # Assuming your model is saved as a .pkl file

app = Flask(__name__)

# Load your pre-trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html", predicted_cost=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve from data
    loan_amount_term = int(request.form['loan_amount_term'])
    applicantincome = float(request.form['applicantincome'])
    loan_amount = float(request.form['loan_amount'])
    credit_history = int(request.form['credit_history'])
    dependent= int(request.form['dependent'])

    # Placeholder prediction logic (replace with actual model inference)
    if loan_amount_term > 600 and applicantincome > 30000 and loan_amount < applicantincome * 0.5:
        prediction = "Loan Approved"
    else:
        prediction = "Loan Denied"

    # Render the template with the prediction result
    return render_template('index.html', prediction_text=prediction)


if __name__ == "__main__":
    app.run(debug=True)