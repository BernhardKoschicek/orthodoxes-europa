from flask import render_template

from orthodoxes_europa import app


@app.route('/öffentlichkeitsarbeit')
def öffentlichkeitsarbeit():
    return render_template('arbeit.html')
