from flask import render_template

from orthodoxes_europa import app


@app.route('/verein')
def verein():
    return render_template('verein.html')
