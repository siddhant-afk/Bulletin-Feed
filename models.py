from init import db

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password = db.Column(db.String(length=60),nullable = False)
    topics = db.Column(db.String())
    location = db.Column(db.String())


    def __repr__(self):
        return self.email_address