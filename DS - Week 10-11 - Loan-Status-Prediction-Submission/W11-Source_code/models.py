from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_bcrypt import Bcrypt
from flask import Flask, request, jsonify, render_template



app = Flask(__name__, template_folder='templates')


ENV = 'dev'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost:3306/login_store'
app.config['SECRET_KEY'] = 'giveanysceretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Create tables in the database
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    

class User_information(db.Model, UserMixin):
    __tablename__='User_information'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    Gender = db.Column(db.String(10), nullable=False)
    Married = db.Column(db.String(5), nullable=False)
    Dependents = db.Column(db.Integer, nullable=False)
    Education = db.Column(db.String(12), nullable=False)
    Self_employed = db.Column(db.String(5), nullable=False)
    Applicant_income = db.Column(db.Integer, nullable=False)
    Coapplicantincome = db.Column(db.Integer, nullable=False)
    Loanamount = db.Column(db.Integer, nullable=False)
    Loan_amount_term = db.Column(db.Integer, nullable=False)
    Credit_history = db.Column(db.String(3), nullable=False)
    Property_area = db.Column(db.String(10), nullable=False)
    Application_status = db.Column(db.String(15), nullable=False)

db.create_all()
