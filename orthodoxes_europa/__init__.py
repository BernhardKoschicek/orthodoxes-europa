from flask import Flask, Response, request

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')  # type: ignore
app.config.from_pyfile('production.py')  # type: ignore

from orthodoxes_europa.util import util, filters
from orthodoxes_europa.views import arbeit, download, geoportal, about, kontakt, projekte, team, \
    verein, index


@app.before_request
def before_request():
    if request.path.startswith('/static'):
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response: Response) -> Response:
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


app.register_blueprint(filters.blueprint)


if __name__ == "__main__":  # pragma: no cover
    app.run()
