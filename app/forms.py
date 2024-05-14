from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField, validators, PasswordField, Form, FileField
from wtforms.validators import DataRequired, Optional, InputRequired, Length, EqualTo, ValidationError, Email
from .models import User
from flask_wtf.file import FileRequired, FileAllowed

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
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    mileage = IntegerField('Mileage', validators=[DataRequired()])
    battery_capacity = IntegerField('Battery Capacity (in kWh)', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    price = FloatField('Price ($)', validators=[DataRequired()])
    doors = IntegerField('Number of Doors', validators=[DataRequired()])
    car_type = SelectField('Car Type', choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe')], validators=[DataRequired()])
    top_speed = IntegerField('Top Speed (km/h)', validators=[DataRequired()])
    acceleration = FloatField('0-100 km/h Acceleration (seconds)', validators=[DataRequired()])
    image = FileField('Car Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Add Listing')