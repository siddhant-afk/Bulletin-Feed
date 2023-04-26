from flask import Flask,render_template, redirect,url_for,flash,get_flashed_messages,request
from models import User
from forms import RegisterForm, LoginForm
from init import db,app
from flask_login import login_user,logout_user,login_required
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

location="in"
language="en"




@app.route("/feed")
@login_required
def home():

    general= f"https://newsapi.org/v2/top-headlines?category=general&language={language}&apiKey={API_KEY}"
    tech = f"https://newsapi.org/v2/top-headlines?country={location}&category=technology&language={language}&apiKey={API_KEY}"
    buiness = f"https://newsapi.org/v2/top-headlines?country={location}&category=business&language={language}&apiKey={API_KEY}"
    sports = f"https://newsapi.org/v2/top-headlines?country={location}&category=sports&language={language}&apiKey={API_KEY}"
    entertainment = f"https://newsapi.org/v2/top-headlines?country={location}&category=entertainment&language={language}&apiKey={API_KEY}"
    health = f"https://newsapi.org/v2/top-headlines?country={location}&category=health&language={language}&apiKey={API_KEY}"
    science = f"https://newsapi.org/v2/top-headlines?country={location}&category=science&language={language}&apiKey={API_KEY}"
    local = f"https://newsapi.org/v2/top-headlines?country={location}&country={location}&apiKey={API_KEY}"

    response = requests.get(general).json()
    

    tech_news  =requests.get(tech).json()['articles']
    sports_news  =requests.get(sports).json()['articles']
    local_news  =requests.get(local).json()['articles']

    return render_template('feed.html', articles = response["articles"],tech_news = tech_news,sports_news=sports_news, local_news=local_news)


@app.route("/register", methods = ['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(email_address = form.email_address.data,
                        password = form.password1.data)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(err)
    
    return render_template('register.html', form=form )


@app.route("/login",methods = ["GET","POST"])
def login():
    error=""
    form = LoginForm()
    if form.validate_on_submit():
        
        attempted_user = User.query.filter_by(email_address = form.email_address.data).first()
        if attempted_user and attempted_user.check_password(attempted_password = form.password.data):
            login_user(attempted_user)
            flash("Successfully Logged In!")
            return redirect(url_for('home'))
        else:
            error = "Wrong credentials. Please try again."
    
            
    return render_template('login.html',form=form,error = error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/preferences', methods=["POST"])
def preferences():
    if request.method == "POST":
        if request.form.get('country'):
            global location 
            location = request.form.get('country')
        if request.form.get('language'):
            global language
            language= request.form.get('language')
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


