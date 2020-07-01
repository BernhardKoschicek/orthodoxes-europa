from flask import render_template

from orthodoxes_europa import app


@app.route('/')
def home() -> str:
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
