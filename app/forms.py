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
    if session['letter'] != field.data[0]:
        raise ValidationError(f"I don't think '{field.data}' starts with the letter '{session['letter']}'. Try again.")


class WordForm(FlaskForm):
    word = StringField('Your word', validators=[DataRequired(), my_word_check])
    submit = SubmitField('Submit word')


def my_gratitude_check(_, field):
    ps = PorterStemmer()
    if ps.stem(session['word']) not in field.data:
        raise ValidationError(f"You didn't use the word '{session['word']}'. Try again.")


class GratitudeForm(FlaskForm):
    gratitude = StringField('Your response', validators=[DataRequired(), my_gratitude_check])
    submit = SubmitField('Submit gratitude')
