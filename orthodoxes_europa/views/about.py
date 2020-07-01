from flask import render_template

from orthodoxes_europa import app


@app.route('/about')
def about():
    return render_template('about.html')
