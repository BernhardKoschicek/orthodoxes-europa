from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app


@app.route('/team')
def team() -> str:
    team_ = OrderedDict([
        ('Sandra Wabnitz', {
            'id': '1',
            'email': 'Sandra.Wabnitz@oeaw.ac.at',
            'function': 'Research',
            'text': """Bachelorstudium Geschichte an der Universität Wien. Anschließend Studium des
             Masters Geschichtsforschung, historische Hilfswissenschaften und Archivwissenschaften
              am Institut für Österreichische Geschichtsforschung der Universität Wien;
               Masterarbeit über die Integration der Barbaren in die lateinische und chinesische
                Historiographie des Frühmittelalters.""",
            'img': 'sandra.jpg',
        }),
        ('Itana Ćupić', {
            'id': '2',
            'email': 'cupicitana@gmail.com',
            'function': 'Research',
            'text': """BSc. in Economics, Department of Tourism (2013, Singidunum Universität,
             Belgrad, Serbien). Masterstudium CREOLE – Cultural Differences and Transnational
              Processes am Institut für Sozial- und Kulturanthropologie der Universität Wien
               (seit 2018)
Initiatorin und Ko-Autorin von „Montenegrins in Austria“, in dessen Rahmen die wissenschaftliche
 Untersuchung mit Bildmaterial „Petar II. Petrović Njegoš in Wien – Der Weg zum Druck des 
 Bergkranzes“ veröffentlicht wurde. Das Projekt wurde von der Botschaft Montenegros in Österreich,
  dem Außenministerium und dem Kulturministerium Montenegros unterstützt, die begleitende Publikation
   von der Nationalbibliothek von Montenegro veröffentlicht (2019, Cetinje, Montenegro).
""",
            'img': 'itana.jpg',
        }),
        ('Rainer Simon', {
            'id': '3',
            'email': 'Rainer.Simon@ait.ac.at',
            'function': 'App Deveolpment',
            'text': """Rainer Simon is a Senior Scientist at the AIT Austrian Institute of 
            Technology. He holds a master’s in telecommunications engineering and a doctorate in 
            computer science from the Vienna University of Technology. Rainer has been working in 
            the field of multimedia information management and retrieval for more than 10 years,
            with a particular focus on technologies and user interfaces that process and visualize
            geospatial information. His current research interest is in the application of Linked 
            (Geo) Data methods and visualization techniques in the Digital Humanities and Digital 
            Librarydomains. Rainer has been involved in several national and international research 
            projects, published various papers in his area, and served as a programme committee 
            member and reviewer for relevant scientific workshops and publications in the field.
            """,
            'img': 'rainer.jpg',
        }),
        ('Bernhard Koschicek', {
            'id': '4',
            'email': 'bernhard.koschicek@oeaw.ac.at',
            'function': 'Backend Development',
            'text': "",
            'img': 'bernhard.png',
        }),
    ])
    return render_template('team.html', team=team_)