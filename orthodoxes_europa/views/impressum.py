from flask import render_template

from orthodoxes_europa import app


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')
