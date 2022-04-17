from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm
import os

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///peertrade.db'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
class Users(db.Model):
    name = db.Column(db.String(), nullable = False, unique = False)
    email = db.Column(db.String(), primary_key = True)
    pw = db.Column(db.String(length = 20), nullable = False)

@app.route('/')
@app.route('/homepage')
def home():
    return render_template('homepage.html', title = 'Home')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["GET","POST"])
def login():
    
    return render_template('login.html', title = 'Login')
    

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(name = form.username.data,
        email = form.email_address.data, pw = form.password1.data)
        db.session.commit()
        return redirect(url_for('index'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg}')
    return render_template('signup.html', form = form, title = "Sign Up")

@app.route('/ourteam')
def ourteam():
    return render_template('ourteam.html', title = "Our Team")


if __name__ == "__main__":
    app.run(debug = True)