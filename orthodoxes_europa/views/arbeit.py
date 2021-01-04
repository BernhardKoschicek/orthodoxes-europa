from collections import OrderedDict

from flask import render_template, url_for

from orthodoxes_europa import app


@app.route('/öffentlichkeitsarbeit')
def öffentlichkeitsarbeit():
    public = OrderedDict([
        ('Kathpress', {
            'type': 'Zeitungsartikel',
            'date': '08. Dezember 2020',
            'title': 'Auf den Spuren orthodoxer Weltkriegsflüchtlinge in Hollabrunn',
            'description': """<p>Die kathpress (Katholische Presseagentur Österreich) berichtet in ihrer
             Information Orthodoxie (Ausgabe Nr. 76, 8. Dezember 2020, Seite 7;
              <a href="https://www.kathpress.at/goto/meldung/1964124/Auf_den_Spuren_orthodoxer_Weltkriegsfl__chtlinge_in_Hollabrunn"
               target="_blank">https://www.kathpress.at/goto/meldung/1964124/Auf_den_Spuren_orthodoxer_Weltkriegsfl__chtlinge_in_Hollabrunn</a>)
                umfassend über unser Forschungsprojekt "Auf der Flucht in der Monarchie – das Schicksal
                 der orthodoxen Flüchtlinge im Lager Oberhollabrunn (1914-1918)".
                </p>
                <p>Bitte sehen Sie dazu im Detail folgenden <a href="{url}" target="_blank">Artikel</a> 
                </p>
                """.format(url=url_for('static',
                                       filename='repository/Kathpress_Orthodoxie_Flüchtlinge_Hollabrunn.pdf'))}),
        ('Le Monde', {
        'type': 'Zeitungsartikel',
        'date': '05. Juni 2020',
        'title': 'Vienne, impératrice de l’Est',
        'description': """<p>Die bekannte französische Tageszeitung Le Monde hat einen Beitrag über
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
