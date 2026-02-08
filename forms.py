from flask_wtf import FlaskForm
from wtforms import StringField , EmailField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired , Length , EqualTo , Regexp , Email



class RegisterForm(FlaskForm):
    fname = StringField("First Name" , validators=[DataRequired() , Length(min=2 , max=25)])
    lname = StringField("Last Name" , validators=[DataRequired() , Length(min=2 , max=25)])
    username = StringField(" UserName" , validators=[DataRequired() , Length(min=2 , max=25)])
    email = EmailField("Email" , validators=[DataRequired() , Email()])
    password = PasswordField("Password" , validators=[DataRequired() , Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            )])
    confirm_password = PasswordField("Confirm Password" , validators=[DataRequired() , EqualTo("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = EmailField("Email" , validators=[DataRequired() , Email()])
    password = PasswordField("Password" , validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
