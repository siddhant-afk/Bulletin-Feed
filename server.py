from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


class Preference(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    topics = db.Column(db.String())
    location = db.Column(db.String())


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/feed")
def home():
    return render_template('feed.html')



if __name__ == '__main__':
    app.run(debug=True)

