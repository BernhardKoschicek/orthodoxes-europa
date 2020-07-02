from flask import Flask, request
1/0

app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config.default')  # type: ignore
# app.config.from_pyfile('production.py')  # type: ignore

from orthodoxes_europa.util import filters, util
from orthodoxes_europa.views import arbeit, download, geoportal, about, kontakt, projekte, team, \
    verein, index


@app.before_request
def before_request():
    if request.path.startswith('/static'):
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


app.register_blueprint(filters.blueprint)

if __name__ == "__main__":  # pragma: no cover
    app.run()
