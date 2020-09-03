from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app


@app.route('/team')
def team() -> str:
    team_ = OrderedDict([
        ('Peter Fraundorfer', {
            'id': '1',
            'email': 'Peter.Fraundorfer@oeaw.ac.at',
            'function': 'Forschung',
            'text': """Bachelorstudium Geschichte an der Universität Wien. Anschließend
            Studium des Masters Geschichtsforschung, historische
            Hilfswissenschaften und Archivwissenschaften am Institut für
            Österreichische Geschichtsforschung; Masterarbeit: Das literarische
            Nachleben des heiligen Rupert: Die hoch- und spätmittelalterlichen
            Vitae Ruperti
            """,
            'img': 'peter.jpg',
        }),
        ('Verena Demel ', {
            'id': '2',
            'email': '',
            'function': 'Forschung',
            'text': """ """,
            'img': 'blank.png',
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
            'function': 'Backend Development (ehrenamtlich)',
            'text': "",
            'img': 'bernhard.png',
        }),
        ('Sandra Wabnitz', {
            'id': '5',
            'email': 'Sandra.Wabnitz@oeaw.ac.at',
            'function': 'Forschung (ehrenamtlich)',
            'text': """Bachelorstudium Geschichte an der Universität Wien. Anschließend Studium des
         Masters Geschichtsforschung, historische Hilfswissenschaften und Archivwissenschaften
          am Institut für Österreichische Geschichtsforschung der Universität Wien;
           Masterarbeit über die Integration der Barbaren in die lateinische und chinesische
            Historiographie des Frühmittelalters.""",
            'img': 'sandra.jpg',
        }),
        ('Mihailo Popović ', {
            'id': '6',
            'email': 'mihailop@hotmail.com',
            'function': 'Projektleiter',
            'text': """Seit meinem Studium der Byzantinistik und Neogräzistik sowie 
            südosteuropäischen Geschichte an der Universität Wien interessiere ich mich für die 
            mittelalterlichen und neuzeitlichen politischen, geistlichen und kulturellen Beziehungen
             zwischen unserem Land und Südosteuropa. Ich möchte mit meiner wissenschaftlichen Arbeit
              das gegenseitige Verständnis und Kennenlernen fördern sowie Brücken zwischen Menschen
               und Ländern bauen. In einem sich vereinenden Europa ist meiner Meinung nach ein
                solcher Dialog unerläßlich.""",
            'img': 'mihailo.jpg',
        }),

    ])
    return render_template('team.html', team=team_)
