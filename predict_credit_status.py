import joblib


def predict_credit_status(reports, expenditure, age, income):
    trained_model = joblib.load("model.joblib")
    prediction = trained_model.predict([[reports, expenditure, age, income]])
    return prediction
