from app import app

import random
import string

from flask import flash, render_template, request, session
from app.forms import WordForm


def random_letter() -> str:
    this_letter = random.choice(string.ascii_lowercase)
    return this_letter


@app.route('/')
@app.route('/index')
def index():
    response = '<p>Hello world</p>' \
               '<a href="/letter">Click here to go to the next page.</a>'
    return response


@app.route('/letter', methods=['GET', 'POST'])
def letter():
    if request.method == 'GET':
        session['letter'] = random_letter()
    form = WordForm()
    if request.method == 'POST':
        if form.validate():
            flash(f'got it: {form.word.data}')

    return render_template(
        'letter.html',
        letter=session['letter'],
        form=form
    )
