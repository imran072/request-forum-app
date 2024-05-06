from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Optional

class SearchForm(FlaskForm):
    make = StringField('Make', validators=[Optional()])
    model = StringField('Model', validators=[Optional()])
    min_price = FloatField('Minimum Price', validators=[Optional()])
    max_price = FloatField('Maximum Price', validators=[Optional()])
    submit = SubmitField('Search')
