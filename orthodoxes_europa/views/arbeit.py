from flask import render_template

from orthodoxes_europa import app


@app.route('/oeffentlichkeitsarbeit')
def oeffentlichkeitsarbeit():
    return render_template('arbeit.html')
