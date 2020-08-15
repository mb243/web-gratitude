from app import app

import random
import string

from flask import redirect, render_template, request, session, url_for
from app.forms import WordForm, GratitudeForm


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
def letter() -> str:
    if request.method == 'GET':
        session['letter'] = random_letter()
    form = WordForm()
    if request.method == 'POST':
        if form.validate():
            session['word'] = form.word.data
            return redirect(url_for('gratitude'))
    return render_template(
        'letter.html',
        letter=session['letter'],
        form=form
    )


@app.route('/gratitude', methods=['GET', 'POST'])
def gratitude() -> str:
    form = GratitudeForm()
    if request.method == 'POST':
        if 'word' not in session:
            return redirect(url_for('letter'))
        if form.validate():
            return redirect(url_for('thanks'))
    return render_template(
        'gratitude.html',
        word=session['word'],
        form=form
    )


@app.route('/thanks')
def thanks() -> str:
    return render_template('thanks.html')
