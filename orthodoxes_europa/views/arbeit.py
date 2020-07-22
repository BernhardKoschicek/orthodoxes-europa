from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app


@app.route('/öffentlichkeitsarbeit')
def öffentlichkeitsarbeit():
    public = OrderedDict([('Le Monde', {
        'type': 'Zeitungsartikel',
        'date': '05.Juni 2020',
        'title': 'Vienne, impératrice de l’Est',
        'description': """<p>Die bekannte französische Tageszeitung Le Monde hat einen Beitrag über
        die Bedeutung der Stadt Wien für die Menschen in Ost- und Südosteuropa im Lauf der
         Vergangenheit und Gegenwart im Druck und online veröffentlicht. Darin kommt unter
          anderem Mihailo Popović zum digitalen Geoportal und der Geschichte der Wiener Serben zu
           Wort. Hier im Auszug:</p>
           <citation> Pour leur remémorer leur passé, l’historien autrichien d’origine serbe
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
                    l’est simplement redevenue. </citation>
                    <p>Weitere Informationen unter: <a href="https://www.lemonde.fr/m-le-mag/article/2020/06/05/vienne-imperatrice-de-l-est_6041894_4500055.html" target="_blank">
                    https://www.lemonde.fr/m-le-mag/article/2020/06/05/vienne-imperatrice-de-l-est_6041894_4500055.html</a></p>
        """
    })
                          ])

    return render_template('arbeit.html', public=public)
