from flask import render_template

from orthodoxes_europa import app


@app.route('/download')
def download():
    return render_template('download.html')
