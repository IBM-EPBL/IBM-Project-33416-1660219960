from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from project.models import User
import email_validator #don't remove

class SignupForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=20)],render_kw={"placeholder": "Username"})
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField("Password",validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField("Sign Up")
    
    def validate_username(self, username):
        username = User.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError("This username is already taken please try new  username")
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
             raise ValidationError("This email is already taken please try new email id")


class SignInForm(FlaskForm):
   
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login")