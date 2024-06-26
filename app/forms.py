from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, HiddenField, TextAreaField, IntegerField, SubmitField, FloatField, SelectField, validators, PasswordField, Form, FileField
from wtforms.validators import DataRequired, Optional, InputRequired, Length, EqualTo, ValidationError, Email, NumberRange
from .models import User
from flask_wtf.file import FileRequired, FileAllowed

class ReplyForm(FlaskForm):
    recipient = StringField('Recipient', validators=[DataRequired()])
    body = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class OfferForm(FlaskForm):
    recipient = HiddenField('Recipient', validators=[DataRequired()])
    vehicle_id = HiddenField('Vehicle ID', validators=[DataRequired()])
    amount = DecimalField('Offer Amount', validators=[DataRequired()])
    submit = SubmitField('Send Offer')


class MessageForm(FlaskForm):
    recipient = StringField('Recipient', validators=[DataRequired()])
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
        
def validate_alphabetic(form, field):
    if not field.data.isalpha():
        raise ValidationError('Field must contain only alphabetic characters.')

def validate_float(form, field):
    try:
        float(field.data)
    except ValueError:
        raise ValidationError('Please enter a decimal number.')

class AddListingForm(FlaskForm):
    make = SelectField('Make', validators=[DataRequired()], choices=[])
    model = SelectField('Model', validators=[DataRequired()], choices=[])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1950, max=2024)])
    mileage = IntegerField('Mileage', validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    battery_capacity = IntegerField('Battery Capacity (kWh)', validators=[DataRequired(), NumberRange(min=0, max=1000)])
    color = StringField('Color', validators=[DataRequired(), validate_alphabetic])
    price = IntegerField('Price ($)', validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    doors = IntegerField('Doors', validators=[DataRequired(), NumberRange(min=1, max=5)])
    car_type = StringField('Car Type', validators=[DataRequired(), validate_alphabetic])
    top_speed = IntegerField('Top Speed (km/h)', validators=[DataRequired(), NumberRange(min=0, max=300)])
    acceleration = FloatField('0-100 km/h Acceleration (seconds)', validators=[DataRequired(), NumberRange(min=0, max=60), validate_float])
    image = FileField('Car Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    submit = SubmitField('Add Listing')
    
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Reset Password')