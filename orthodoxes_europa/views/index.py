from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app



@app.route('/')
def home() -> str:
    front_menu = OrderedDict([
        ('projekte', {
            'id': '1',
            'image': 'projekte.jpg',
            'title': 'Projekte',
            'subtitle': 'Überischt über alle Projekte'
        }),
        ('öffentlichkeitsarbeit', {
            'id': '2',
            'image': 'oeffentlich.jpg',
            'title': 'Öffentlichkeitsarbeit',
            'subtitle': 'Veranstaltungen, Vorträge, Veröffentlichungen und Pressemeldungen'
        }),
        ('geoportal', {
            'id': '3',
            'image': 'Österreich-Europa-Karte.png',
            'title': 'Geoportal',
            'subtitle': 'Digitale Geoportal der Orthodoxen in Österreich'
        }),
        ('team', {
            'id': '4',
            'image': 'team.jpg',
            'title': 'Team',
            'subtitle': 'Vorstellung des Teams'
        })
    ])

    return render_template('home.html', front_menu=front_menu)


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
