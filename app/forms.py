from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, FloatField, SelectField, validators, PasswordField, Form, FileField
from wtforms.validators import DataRequired, Optional, InputRequired, Length, EqualTo, ValidationError, Email, NumberRange
from .models import User
from flask_wtf.file import FileRequired, FileAllowed


class MessageForm(FlaskForm):
    recipient = SelectField('Recipient', coerce=int, validators=[DataRequired()])
    body = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Send')

class SearchForm(FlaskForm):
    make = StringField('Make', validators=[Optional()])
    model = StringField('Model', validators=[Optional()])
    min_price = FloatField('Minimum Price', validators=[Optional()])
    max_price = FloatField('Maximum Price', validators=[Optional()])
    submit = SubmitField('Search')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose a different one.')
        
class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class AddListingForm(FlaskForm):
    make = SelectField('Make', validators=[DataRequired()], choices=[])
    model = SelectField('Model', validators=[DataRequired()], choices=[])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1886)])
    mileage = IntegerField('Mileage', validators=[DataRequired()])
    battery_capacity = IntegerField('Battery Capacity (kWh)', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    price = IntegerField('Price ($)', validators=[DataRequired()])
    doors = IntegerField('Doors', validators=[DataRequired(), NumberRange(min=1, max=5)])
    car_type = StringField('Car Type', validators=[DataRequired()])
    top_speed = IntegerField('Top Speed (km/h)', validators=[DataRequired()])
    acceleration = FloatField('0-100 km/h Acceleration (seconds)', validators=[DataRequired()])
    image = FileField('Car Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    submit = SubmitField('Add Listing')

