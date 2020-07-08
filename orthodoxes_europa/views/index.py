from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app



@app.route('/')
def home() -> str:
    front_menu = OrderedDict([
        ('projekte', {
            'id': '1',
            'image': 'ratzenstadtl.jpg',
            'title': 'Projekte',
            'subtitle': 'Veranstaltungen, Vorträge, Veröffentlichungen und Pressemeldungen'
        }),
        ('öffentlichkeitsarbeit', {
            'id': '2',
            'image': 'ratzenstadtl.jpg',
            'title': 'Öffentlichkeitsarbeit',
            'subtitle': 'Veranstaltungen, Vorträge, Veröffentlichungen und Pressemeldungen'
        }),
        ('geoportal', {
            'id': '3',
            'image': 'Österreich-Europa-Karte.png',
            'title': 'Geoportal',
            'subtitle': 'Veranstaltungen, Vorträge, Veröffentlichungen und Pressemeldungen'
        }),
        ('team', {
            'id': '4',
            'image': 'leibnitz_transport.jpg',
            'title': 'Team',
            'subtitle': 'Veranstaltungen, Vorträge, Veröffentlichungen und Pressemeldungen'
        })
    ])

    return render_template('home.html', front_menu=front_menu)


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
