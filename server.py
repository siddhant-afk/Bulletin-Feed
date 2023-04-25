from flask import Flask,render_template, redirect,url_for,flash,get_flashed_messages
from models import User
from forms import RegisterForm
from init import db,app





    



@app.route("/feed")
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


@app.route("/login")
def login():
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)


