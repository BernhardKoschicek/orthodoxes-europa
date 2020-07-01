from flask import render_template

from orthodoxes_europa import app


@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')
