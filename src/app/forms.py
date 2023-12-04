from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, BooleanField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class PartNumForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])

class AnswerButtonForm(FlaskForm):
    pass
