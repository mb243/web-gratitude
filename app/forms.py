import enchant

from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

from nltk.stem import PorterStemmer


def my_word_check(_, field):
    d = enchant.Dict("en_US")
    if not d.check(field.data):
        raise ValidationError("I don't know that word. Please choose another.")
    if session['letter'] != field.data[0].lower():
        raise ValidationError(f"I don't think '{field.data}' starts with the letter '{session['letter']}'. Try again.")


class WordForm(FlaskForm):
    word = StringField('Your word', validators=[DataRequired(), my_word_check])
    submit = SubmitField('Submit')


def my_gratitude_check(_, field):
    ps = PorterStemmer()
    if ps.stem(session['word']) not in field.data:
        raise ValidationError(f"I don't think you used a word like '{session['word']}'. Try again.")


class GratitudeForm(FlaskForm):
    gratitude = StringField('Your response', validators=[DataRequired(), my_gratitude_check])
    submit = SubmitField('Submit')
