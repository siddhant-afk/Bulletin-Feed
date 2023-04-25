from flask import Flask,render_template, redirect,url_for,flash,get_flashed_messages
from models import User
from forms import RegisterForm, LoginForm
from init import db,app
from flask_login import login_user,logout_user,login_required

@app.route("/feed")
@login_required
def home():
    return render_template('feed.html')


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



if __name__ == '__main__':
    app.run(debug=True)


