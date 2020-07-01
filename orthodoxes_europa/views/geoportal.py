from flask import render_template

from orthodoxes_europa import app


@app.route('/geoportal')
def geoportal():
    return render_template('geoportal.html')
