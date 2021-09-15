from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app


@app.route('/öffentlichkeitsarbeit')
def öffentlichkeitsarbeit():
    public = OrderedDict([
        ('Digitale Medien Vortrag', {
            'id': 'DigitaleMedien',
            'type': 'Vortrag',
            'date': '02. Juli 2021',
            'title': 'Digitale Medien auf den Spuren der Orthodoxen in Wien: Das Online Geoportal der Geschichte der SerbInnen in Wien (1741–1918) und der Orthodoxen in Österreich',
            'image': 'digitales_portal_vortrag.jpg',
            'description': """<p>Am 2. Juli 2021 hat der Verein der Serben in 
                der Republik Österreich mit ihrem Präsidenten Aleksandar Stanković
                zu einem Vortrag von Doz. Dr. Mihailo St. Popović und Zlatan Stojadinović,
                 BA mit dem Titel "Digitale Medien auf den Spuren der Orthodoxen 
                 in Wien: Das Online Geoportal der Geschichte der SerbInnen in Wien...</p>""",
            'text': """<p>
            Am 2. Juli 2021 hat der Verein der Serben in der Republik Österreich 
            mit ihrem Präsidenten Aleksandar Stanković zu einem Vortrag von Doz. 
            Dr. Mihailo St. Popović und Zlatan Stojadinović, BA mit dem Titel 
            "Digitale Medien auf den Spuren der Orthodoxen in Wien: Das Online 
            Geoportal der Geschichte der SerbInnen in Wien (1741–1918) und der 
            Orthodoxen in Österreich" eingeladen. An diesem Publikumsabend haben 
            die Vortragenden ihre wissenschaftlichen Resultate und vor allem 
            deren Nutzen für die interessierte Öffentlichkeit vorgestellt. Ein 
            besonderes Anliegen war ihnen dabei, die panorthodoxe Dimension 
            dieser Arbeit anzusprechen, weil Mihailo Popović in der Zwischenzeit 
            eine private Forschungsinitiative und Plattform unter dem Namen 
            "Digitales Geoportal der Geschichte der Orthodoxen in Österreich" 
            (<a href="https://orthodoxes-europa.at/">https://orthodoxes-europa.at/</a>) begründet hat, mit der er in 
            wissenschaftlichen Subprojekten weiterführende Themen zu den 
            Orthodoxen in Österreich erforscht und ebenfalls online zugänglich 
            macht.</p><p>
            Der Vortrag wurde live online übertragen. Die Aufzeichnung ist 
            abrufbar unter: 
            <a href="https://www.facebook.com/ljubisa.dimitrijevic.75/videos/490396565588455/">
            https://www.facebook.com/ljubisa.dimitrijevic.75/videos/490396565588455/
            </a>
            </p>
            """,
            'attachment': '<iframe src="https://www.facebook.com/plugins/video.php?height=314&href=https%3A%2F%2Fwww.facebook.com%2Fljubisa.dimitrijevic.75%2Fvideos%2F490396565588455%2F&show_text=false&width=560&t=0" width="600" height="400" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>'
        }),
        ('Streifzug', {
            'id': 'Streifzug',
            'type': 'Vortrag',
            'date': '16. Jänner 2021',
            'title': 'Streifzug durch die Religionen',
            'image': 'streifzug.jpg',
            'description': """Im Rahmen der Online-Firmvorbereitung des Entwicklungsraums "Donaustadt-Mitte"
             durfte Mihailo Popović den römisch-katholischen Jugendlichen mit Vertretern anderer
              Weltreligionen am 16. Jänner 2021 Rede und Antwort stehen....
                """,
            'text': """Im Rahmen der Online-Firmvorbereitung des Entwicklungsraums "Donaustadt-Mitte"
             durfte Mihailo Popović den römisch-katholischen Jugendlichen mit Vertretern anderer
              Weltreligionen am 16. Jänner 2021 Rede und Antwort stehen. An diesem Abend wurden
               vor allem besondere Momente bzw. Rituale und Symbole in der Glaubensgemeinschaft
                sowie Initiationsriten in Bezug auf das Erwachsen werden erörtert. Die Jugendlichen
                 zeigten großes Interesse an allen vertretenen Religionen und stellten zahlreiche
                  Fragen.""",
            'attachment': '<embed src="static/repository/Streifzug_durch_die_Religionen.pdf" width="100%" height="600px" />'
        }),
        ('Weihnachten', {
            'id': 'Weihnachten',
            'type': 'Video',
            'date': '07. Jänner 2021',
            'title': 'Warum feiern die orthodoxen Kirchen am 7. Jänner Weihnachten?',
            'image': 'weihnachten.jpg',
            'description': """Zum Jahreswechsel hat Mihailo Popović für die Salesianische
             Jugendbewegung Österreich ein Interview gegeben. In der Sendung "Frag den Don" von P.
              Johannes Haas von den Salesianern Don Boscos hat er über das Thema "Warum feiern
               die orthodoxen Kirchen am 7. Jänner Weihnachten?" gesprochen...
                """,
            'text': """Zum Jahreswechsel hat <b>Mihailo Popović</b> für die <b><a href='https://www.donbosco4youth.at/' target='_blank'>Salesianische Jugendbewegung
             Österreich</a></b> ein Interview gegeben. In der Sendung "Frag den Don" von P. Johannes Haas
              von den Salesianern Don Boscos hat er über das Thema <b>"Warum feiern die orthodoxen
               Kirchen am 7. Jänner Weihnachten?"</b> gesprochen.<br>
                Sehen Sie dazu bitte folgenden Link: 
                <a href='https://www.youtube.com/watch?v=2McBHjhU_Kg' target='_blank'>https://www.youtube.com/watch?v=2McBHjhU_Kg</a>""",
            'attachment': '<div class="pt-2">'
                          '<iframe width="100%" height="500px" src="https://www.youtube.com/embed/2McBHjhU_Kg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>'
                          '</iframe></div>'
        }),
        ('Kathpress', {
            'id': 'Spuren',
            'type': 'Zeitungsartikel',
            'date': '08. Dezember 2020',
            'title': 'Auf den Spuren orthodoxer Weltkriegsflüchtlinge in Hollabrunn',
            'image': 'spuren.jpg',
            'description': """<p>Die kathpress (Katholische Presseagentur Österreich) berichtet in ihrer
             Information Orthodoxie (Ausgabe Nr. 76, 8. Dezember 2020, Seite 7)
                umfassend über unser Forschungsprojekt "Auf der Flucht in der Monarchie – das Schicksal
                 der orthodoxen Flüchtlinge im Lager Oberhollabrunn (1914-1918)"...
                """,
            'text': """<p>Die kathpress (Katholische Presseagentur Österreich) berichtet in ihrer
         Information Orthodoxie (Ausgabe Nr. 76, 8. Dezember 2020, Seite 7;
          <a href="https://www.kathpress.at/goto/meldung/1964124/Auf_den_Spuren_orthodoxer_Weltkriegsfl__chtlinge_in_Hollabrunn"
           target="_blank" class="wrapword">https://www.kathpress.at/goto/meldung/1964124/Auf_den_Spuren_orthodoxer_Weltkriegsfl__chtlinge_in_Hollabrunn</a>)
            umfassend über unser Forschungsprojekt "Auf der Flucht in der Monarchie – das Schicksal
             der orthodoxen Flüchtlinge im Lager Oberhollabrunn (1914-1918)".
             </p>""",
            'attachment': '<embed src="static/repository/Kathpress_Orthodoxie_Flüchtlinge_Hollabrunn.pdf" width="100%" height="1100px" />'
        }),
        ('Relief', {
            'id': 'Relief',
            'type': 'Zeitungsartikel',
            'date': '18. Mai 2020',
            'title': 'Montenegro im Relief: Terra incognita auf dem Balkan',
            'image': 'relief.jpg',
            'description': """<p>DerStandard veröffentlicht in der Kategorie "Wissens
            -Blogs" einen Beitrag von  Mihailo Popović über die 250m² große Reliefkarte von und in Montenegro,
            die während dem Ersten Weltkrieg von der  k. u. k. Armee erbaut wurde...
                """,
            'text': """<p>
            <a href="https://www.derstandard.at/">DerStandard</a> veröffentlicht in der Kategorie "Wissens
            -Blogs" einen Beitrag von  
            <a href="https://www.derstandard.at/story/2000117505690/montenegro-im-relief-terra-incognita-auf-dem-balkan?fbclid=IwAR2blOQJUHrKWrQrAycc-3SIoMHzksp1HFqz3eX-jW5EU5S7gmqzRiLrtmk">Mihailo Popović, "Montenegro im Relief: Terra incognita auf dem Balkan"</a>, über die 250m² große Reliefkarte von und in Montenegro,
            die während dem Ersten Weltkrieg von der  k. u. k. Armee erbaut wurde.
             </p>"""
        }),
        ('Le Monde', {
            'id': 'Vienne',
            'type': 'Zeitungsartikel',
            'date': '05. Juni 2020',
            'title': 'Vienne, impératrice de l’Est',
            'image': 'balkan.jpg',
            'description': """<p>Die bekannte französische Tageszeitung Le Monde hat einen Beitrag über
            die Bedeutung der Stadt Wien für die Menschen in Ost- und Südosteuropa im Lauf der
             Vergangenheit und Gegenwart im Druck und online veröffentlicht. Darin kommt unter
              anderem Mihailo Popović zum digitalen Geoportal und der Geschichte der Wiener Serben zu
               Wort...""",
            'text': """<p>Die bekannte französische Tageszeitung Le Monde hat einen Beitrag über
        die Bedeutung der Stadt Wien für die Menschen in Ost- und Südosteuropa im Lauf der
         Vergangenheit und Gegenwart im Druck und online veröffentlicht. Darin kommt unter
          anderem Mihailo Popović zum digitalen Geoportal und der Geschichte der Wiener Serben zu
           Wort. Hier im Auszug:</p>
           <blockquote class="blockquote text-center"><cite> Pour leur remémorer leur passé, l’historien autrichien d’origine serbe
           Mihailo Popovic a créé une application listant toutes les traces historiques de la
            Serbie dans la capitale autrichienne et fait visiter avec passion les églises orthodoxes
             du XVIIIe siècle ou les vieilles boutiques au nom serbe du centre de Vienne. Autant
              d’indices de cette époque où la capitale austro-hongroise « était le centre
               intellectuel et culturel serbe », rappelle cet orthodoxe pratiquant, qui reproche
                tout autant aux Autrichiens de ne pas assez célébrer cette diversité qu’aux
                 ex-Yougoslaves ne pas faire suffisamment d’efforts pour s’intégrer. « On doit
                  combiner les deux mondes, plaide-t-il, en assurant qu’il ne s’agit que d’un retour
                  à la normale après la longue parenthèse des conflits qui ont déchiré l’Europe
                   entre 1914 et 1989. En 1900, Vienne était multiculturelle. Aujourd’hui, elle
                    l’est simplement redevenue. </cite>
                    <footer class="blockquote-footer">Par Jean-Baptiste Chastand (<cite>
                    <a href="https://www.lemonde.fr/m-le-mag/article/2020/06/05/vienne-imperatrice-de-l-est_6041894_4500055.html"
                     target="_blank">https://www.lemonde.fr/m-le-mag/article/2020/06/05/vienne-imperatrice-de-l-est_6041894_4500055.html</a></cite> )</footer>
                    </blockquote>
        """
        })

    ])

    return render_template('arbeit.html', public=public)
