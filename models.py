from init import db,bcrypt
from init import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60),nullable = False)
    topics = db.Column(db.String())
    location = db.Column(db.String())


    def __repr__(self):
        return self.email_address
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,plain_password):
        self.password_hash= bcrypt.generate_password_hash(plain_password).decode('utf-8')
    
    def check_password(self,attempted_password):
        if bcrypt.check_password_hash(self.password_hash,attempted_password):
            return True


