from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, BooleanField
from wtforms.validators import DataRequired


class PasswordsQuestion1Form(FlaskForm):
    common_phrases = BooleanField("Common phrases")
    significant_dates = BooleanField("Using significant dates")
    long_passwords = BooleanField("Using long passwords")
    pet_names = BooleanField("Using pet names")
    random_words = BooleanField("Using random words in passwords")
    submit = SubmitField("Check Answers", validators=[DataRequired()])


class PasswordsQuestion2Form(FlaskForm):
    password123 = BooleanField("password123")
    calendargrapesmug = BooleanField("calendargrapesmug")
    numbers = BooleanField("123456")
    bob2005 = BooleanField("bob2005")
    treefolderbottle = BooleanField("treefolderbottle")
    submit = SubmitField("Check Answers", validators=[DataRequired()])
