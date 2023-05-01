from flask import Blueprint,render_template,request
import pickle
import numpy as np
import sklearn
from flask_login import current_user 
from models import db,User_information

predict_view = Blueprint('prediction', __name__, template_folder="templates")
model = pickle.load(open('model.pkl', 'rb')) # loading the trained model

@predict_view.route('/prediction.enter_details') ## for entering details
def enter_details():
    return render_template('predict.html')

@predict_view.route('/prediction.predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    for i,j in zip(request.form.keys(),request.form.values()):
        if i=="Gender":
            gender = 'male' if j == '1' else 'female'
        elif i=="married":
            married = 'yes' if j == '1' else 'no'
        elif i=="dependents":
            dependents = request.form['dependents']
        elif i=="education":
            education = 'graduate' if j == '1' else 'not graduate'
        elif i=="self_employed":
            self_employed = 'yes' if j == '1' else 'no'
        elif i=="applicantincome":
            applicant_income = request.form['applicantincome']
        elif i=="coapplicantincome":
            coapplicant_income = request.form['coapplicantincome']
        elif i=="loanamount":
            loan_amount = request.form['loanamount']
        elif i=="loan_amount_term":
            loan_amount_term = request.form['loan_amount_term']
        elif i=="credit_history":
            credit_history = 'yes' if j == '1' else 'no'
        elif i=="property_area":
            if j == '0' :
                property_area = 'rural'
            elif j == '1' :
                property_area = 'urban'
            elif j == '2' :
                property_area = 'semiurban'
        
    if prediction[0] == 1:
        application_status = "Approved"
    else:
        application_status = "Not Approved"

    user_information = User_information(user_id=current_user.id,Gender=gender,Married=married,Dependents=dependents,
                                        Education=education,Self_employed=self_employed,Applicant_income=applicant_income,
                                        Coapplicantincome=coapplicant_income,Loanamount=loan_amount,Loan_amount_term=loan_amount_term,
                                        Credit_history=credit_history,Property_area=property_area,Application_status=application_status)
    db.session.add(user_information)
    db.session.commit()

        
    if prediction==0:
        return render_template('predict.html', prediction_text='Sorry:( you are not eligible for the loan ')
    else:
        return render_template('predict.html', prediction_text='Congrats!! you are eligible for the loan')
