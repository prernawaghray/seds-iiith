from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import  login_user, login_required, logout_user, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import pandas as pd
import numpy as np
import mysql.connector
from flask import Flask, request, jsonify, render_template
from predict.predict_views import predict_view
from models import User_information, db, User, app


bcrypt = Bcrypt(app)

## for managing our application and Flask_login to work together
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

## To reload the objects from the user_ids stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


## Create a RegisterForm
class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


## Create a loginform
class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('prediction.enter_details'))
    return render_template('login.html', form=form)


## hashing the password is optional for the learners
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data) ## creates a password hash
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/get_user_count')
def get_user_count():
    return redirect(url_for('user_count'))

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE

@app.route('/statistical_summary', methods=['GET'])
def statistical_summary():
    '''HTML GUI
    Prints the 5-point statistical summary'''

    cnx = mysql.connector.connect(host='localhost',user='root',password='pass',database='login_store')
    cursor = cnx.cursor()    
     
    registered_users = db.session.query(User).count()
    if registered_users != 0:
        sql_query = pd.read_sql_query ('''SELECT * FROM User_information''', cnx)
        df = pd.DataFrame(sql_query, columns=['id','user_id','Gender','Married','Dependents','Education','Applicant_income' 
            ,'Coapplicantincome','Loanamount','Loan_amount_term','Credit_history','Property_area','Application_status'])

        result = df.describe().to_html() 
        
        return result
    else :
        return "No Users Registered yet."

@app.route('/outcome_summary')
def outcome_summary():
    result = db.session.query(User).count()
    approved = User_information.query.filter_by(Application_status='Approved').count()
    percentage_approved = approved*100/result
    return jsonify({'Percantage of users whose loan got approved' : '{:.2f}'.format(percentage_approved)})
    

@app.route('/user_count')
def user_count():
    result = db.session.query(User).count()
    return jsonify({'Number of registered users': result})
    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# register the blueprints
app.register_blueprint(predict_view)

if __name__ == "__main__":
    app.run(debug=True,port=6622)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
