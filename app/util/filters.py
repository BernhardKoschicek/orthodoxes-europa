"""Jinja template filters and menu helpers."""
from collections.abc import Iterable
from typing import Any

import flask
from flask import url_for
from jinja2 import pass_context

from app.data.projects import projects_

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)

INSTITUTES = {
    'ZF': {
        'name': 'Zukunftsfonds',
        'url': 'http://www.zukunftsfonds-austria.at/',
        'logo': 'zf_logo.jpg',
        'member': '',
        'address': ''},
    'ROK': {
        'name': 'Rumänisch-orthodoxe Kirchengemeinde „Auferstehung des Herrn '
                'und hl. Ap. Andreas“',
        'url': 'http://www.rumkirche.at/de/home-page-deutsch/',
        'logo': 'mantuitorul.png',
        'member': 'Erzpriester OStR HS Prof. Dr. Nicolae Dura',
        'address': 'Simmeringer Hauptstr. 161/ Kobelgasse 18<br>1110  '
                   'Wien<br>Österreich'},
    'MT': {
        'name': 'Metropolis von Austria',
        'url': 'http://www.metropolisvonaustria.at/',
        'logo': 'metropolis.png',
        'member': 'S. Em. Metropolit Arsenios von Austria',
        'address': 'Fleischmarkt 13<br>1010 Wien<br>Österreich'},
    'OEAW': {
        'name': 'Austrian Academy of Sciences',
        'url': 'https://www.oeaw.ac.at/',
        'logo': 'oeaw.png',
        'member': '',
        'address': ''},
    'IMAFO': {
        'name': 'Institute for Medieval Research',
        'url': 'https://www.oeaw.ac.at/imafo/',
        'logo': 'imafo.png',
        'member': '',
        'address': ''},
    'ABF': {
        'name': 'Abteilung Byzanzforschung (ABF)',
        'url': 'https://www.oeaw.ac.at/en/byzantine-research/',
        'logo': 'oeaw.jpg',
        'member': 'Österreichische Akademie der Wissenschaften (ÖAW) <br> '
                  'Institut für Mittelalterforschung (IMAFO)',
        'address': 'Hollandstraße 11-13<br> 1020 Wien<br> Österreich'},
    'ACDH': {
        'name': 'Austrian Centre for Digital Humanities and Cultural Heritage',
        'url': 'https://www.oeaw.ac.at/acdh/',
        'logo': 'acdh.png',
        'member': '',
        'address': ''},
    'univie': {
        'name': 'University of Vienna',
        'url': 'https://www.univie.ac.at/',
        'logo': 'uni_vienna.jpg',
        'member': '',
        'address': ''},
    'FWF': {
        'name': 'Austrian Science Fund',
        'url': 'https://www.fwf.ac.at/',
        'logo': 'fwf.png',
        'member': '',
        'address': ''},
    'OeAI': {
        'name': 'Austrian Archaeological Institute',
        'url': 'https://www.oeaw.ac.at/oeai/',
        'logo': 'oeai.png',
        'member': '',
        'address': ''},
    'MA7': {
        'name': 'Wien Kultur (MA 7)',
        'url': 'https://www.wien.gv.at/kultur/abteilung/',
        'logo': 'wien-kultur.png',
        'member': '',
        'address': ''},
    'AIT': {
        'name': 'Austrian Institute of Technology',
        'url': 'https://www.ait.ac.at/',
        'logo': 'ait.jpg',
        'member': '',
        'address': ''},
    'BCM': {
        'name': 'Belgrade City Museum',
        'url': 'http://www.mgb.org.rs/en/',
        'logo': 'bcm.png',
        'member': '',
        'address': ''},
    'NLS': {
        'name': 'National Library of Serbia',
        'url': 'https://www.nb.rs',
        'logo': 'nls.jpg',
        'member': '',
        'address': ''},
    'Biblioteka Matice Srpske': {
        'name': 'Biblioteka Matice Srpske',
        'url': 'http://www.bms.ns.ac.rs/bms101.htm',
        'logo': 'biblioteka_matice_srpske.png',
        'member': '',
        'address': ''},
    'TIB': {
        'name': 'Tabula Imperii Byzantini',
        'url': 'https://tib.oeaw.ac.at',
        'logo': 'tib.png',
        'member': '',
        'address': ''},
    'UAI': {
        'name': 'Union Académique Internationale',
        'url': 'http://www.uai-iua.org/en',
        'logo': 'uai.jpg',
        'member': '',
        'address': ''}}


@pass_context
@blueprint.app_template_filter()
def display_menu(_context: Any, route: str) -> str:
    """Return HTML with the menu and mark appropriate item as selected."""
    html = ''
    items = [
        'projekte', 'öffentlichkeitsarbeit', 'team', 'geoportal',
        'download', 'veröffentlichungen', 'impressum']
    for item in items:
        active = ''
        if route.startswith('/' + item):
            active = 'active'
        if item == 'projekte':
            item_url = url_for(item)
            html += (
                '<div class="nav-item dropdown">'
                f'<a class=" nav-link dropdown-toggle {active}" '
                f'href="{item_url}" id="navbarDropdown" role="button" '
                'data-bs-toggle="dropdown" aria-haspopup="true" '
                f'aria-expanded="false">{item.title()}</a>'
                '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
                f'<a class="dropdown-item" href="{item_url}">Übersicht</a>'
                '<li><hr class="dropdown-divider"></li>')
            for project in projects_:
                p_url = url_for(item, projekt=project, _method='GET')
                p_label = project.replace('-', ' ')
                html += (
                    f'<a class="dropdown-item" href="{p_url}">{p_label}</a>')
            html += '</div></div>'
        else:
            item_url = url_for(item)
            html += (
                f'<a class="nav-item nav-link {active}" href="{item_url}">'
                f'{item.title()}</a>')
    return html


@pass_context
@blueprint.app_template_filter()
def display_institutes(_context: Any, institutes: Iterable[str]) -> str:
    """Render institute logos linked to institute websites."""
    html = ''
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        url = institute['url']
        logo = institute['logo']
        name = institute['name']
        html += (
            f'<a href="{url}" target="_blank">'
            f'<img src="/static/images/institutes/{logo}" alt="{name}" '
            f'title="{name}" style="display: unset;">'
            '</a>')
    return html


@pass_context
@blueprint.app_template_filter()
def display_sponsors(_context: Any, institutes: Iterable[str]) -> str:
    """Render sponsor details including member, address and logo."""
    html = '<div>'
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        name = institute['name']
        member = institute['member']
        address = institute['address']
        url = institute['url']
        logo = institute['logo']
        html += (
            '<div class="row">'
            '<div class="col">'
            f'<h6>{name}</h6>'
            f'<p>{member}</p>'
            f'<p>{address}</p>'
            f'<p><a href="{url}" target="_blank">{url}</a></p>'
            '</div>'
            '<div class="col-sm-4">'
            f'<a href="{url}" target="_blank">'
            f'<img src="/static/images/institutes/{logo}" '
            f'alt="{name}" title="{name}" style="max-height: 200px">'
            '</a>'
            '</div>'
            '</div>')
    return html + '</div>'
