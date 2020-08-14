import enchant

from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired


def my_word_check(form, field):
    d = enchant.Dict("en_US")
    if not d.check(field.data):
        raise ValidationError("I don't know that word. Please choose another.")
    if session['letter'] != field.data[0]:
        raise ValidationError(f"I don't think '{field.data}' starts with the letter '{session['letter']}'. Try again.")


class WordForm(FlaskForm):
    word = StringField('Your word', validators=[DataRequired(), my_word_check])
    submit = SubmitField('Submit word')
