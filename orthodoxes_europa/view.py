from collections import OrderedDict
from flask import render_template
import itertools

from orthodoxes_europa import app
from orthodoxes_europa.data.index import front_menu, home_gallery
from orthodoxes_europa.data.projects import project_gallery, projects_
from orthodoxes_europa.data.public_relations import public
from orthodoxes_europa.data.publications import publications
from orthodoxes_europa.data.software import software
from orthodoxes_europa.data.team import team_



@app.route('/')
def home() -> str:
    return render_template(
        'home.html',
        front_menu=front_menu,
        home_gallery=home_gallery)


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/öffentlichkeitsarbeit')
def öffentlichkeitsarbeit():
    return render_template('public.html', public=public)


@app.route('/veröffentlichungen')
def veröffentlichungen():
    return render_template(
        'veroeffentlichungen.html',
        publications=publications)


@app.route('/download')
def download():
    return render_template(
        'download.html',
        publications=publications,
        software=software,
        category=list(itertools.chain.from_iterable([cat['category'] for id, cat in publications.items()])))


@app.route('/geoportal')
def geoportal():
    return render_template('geoportal.html')


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')


@app.route('/verein')
def verein():
    return render_template('verein.html')


@app.route('/team')
def team() -> str:
    return render_template('team.html', team=team_)


@app.route('/projekte', methods=['GET'])
@app.route('/projekte/<projekt>', methods=['GET'])
def projekte(projekt=None):
    if projekt:
        return render_template(
            'projekt_details/projekt_layout.html',
            projekt=projects_[projekt],
            gallerie=project_gallery)
    else:
        return render_template('projekte.html', projects=projects_)
