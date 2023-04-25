from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length,Email,EqualTo,DataRequired, ValidationError
from models import User



class RegisterForm(FlaskForm):


    def validate_email_address(self,email):
        user = User.query.filter_by(email_address = email.data).first()

        if user:
            raise ValidationError("Email address already exist!")
        
    email_address = StringField(label='email', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='password1', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='password2', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')



class LoginForm(FlaskForm):
    email_address = StringField(label='email', validators=[Email(),DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
