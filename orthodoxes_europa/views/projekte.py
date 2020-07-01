from collections import OrderedDict

from flask import render_template

from orthodoxes_europa import app

projects_ = OrderedDict([
    ('Flucht', {
        'id': '1',
        'image': 'lager_oberhollabrunn.jpg',
        'title': 'Flucht, Gefangenschaft, Neubeginn und Widerstand',
        'subtitle': """Die Orthodoxen in Österreich: Auf der Flucht in der Monarchie – das 
                        Schicksal der orthodoxen Flüchtlinge im Lager Oberhollabrunn""",
        'number': 'Zukunftsfonds der Republik Österreich P19-3804',
        'duration': '1. Juli 2020 bis 1. August 2021 (12 Monate)',
        'pi': 'Priv.-Doz. Mag. Dr. Mihailo Popović',
        'members': ['Sandra Wabnitz', 'Itana Ćupić'],
        'institute': ['MT'],
        'sponsor': ['ZF'],
        'partners': ['MT', 'AIT'],
        'description': """<p>In diesem Projekt richten wir unseren Fokus auf das schwere Los der Zivilbevölkerung im Ersten Weltkrieg (1914-1918) und hier im besonderen auf die östliche Front Österreich-Ungarns in diesem weltumspannenden Konflikt. Mit dem Ausbruch des Ersten Weltkriegs am 28. Juli 1914 gelang es der Armee des Zarenreiches Rußland zunächst, in der Bukowina und in Ostgalizien tief auf das Staatsgebiet Österreich-Ungarns einzudringen. Dies hatte zur Folge, dass die dortige (zu einem beträchtlichen Teil orthodoxe) Bevölkerung floh / fliehen musste und in der Folge in andere Teile der Monarchie evakuiert werden musste. Die Statthalterei von Niederösterreich (damals das Erzherzogtum Österreich unter der Enns) erließ ein Rundschreiben an alle Bezirkshauptmannschaften und fragte an, ob die Möglichkeit zur Aufnahme dieser Kriegsflüchtlinge bestünde. Oberhollabrunn (jetzt Teil der Stadt Hollabrunn, Niederösterreich) war wegen des Bedarfs an Hilfskräften in der Landwirtschaft dazu bereit. Im Februar 1915 befand sich rund eine halbe Million Kriegsflüchtlinge aus Galizien in verschiedenen Teilen der Monarchie, davon rund 25.000 in Niederösterreich. Die große Anzahl von Flüchtlingen auf dem Gebiet von Oberhollabrunn führte schließlich zur Überlegung, ebendort ein eigenes Flüchtlingslager zu errichten. Einer der führenden Initiatoren dieser Idee war der damalige Bürgermeister von Oberhollabrunn, Dr. Rudolf Kolisko (1859-1942, Bürgermeister 1908-1919), der Gemeindegrundstücke südlich bzw. südöstlich des Ortes zur Verfügung stellen wollte, damit diese infrastrukturell zu einem Flüchtlingslager ausgebaut würden, das nach dem Krieg als Stadterweiterungsgebiet (Stichwort: Gartenstadt) einverleibt werden sollte. Das Lager war für 5.000 Flüchtlinge konzipiert. Bürgermeister Kolisko unterstützte die zentralen Behörden der Monarchie tatkräftig im Wege seiner Stadtgemeinde, indem er eine Wasserleitung, einen Hauptsammelkanal und eine Schmalspurbahn vom Stationsgebäude der Nordwestbahn bis zum Lager errichten ließ sowie die Elektrifizierung des Areals gewährleistete. An Unterkünften wurden einerseits Familienhäuser in fester Bauweise und andererseits Baracken aus Holz erbaut. Es entstand eine komplette, autarke Infrastruktur mit Gebäuden für die Lagerverwaltung, mit einer Schule, einer Wäscherei, Werkstätten, Wachhäusern, Ställen für Rinder und Schweine, Wirtschaftsgebäuden, einer Quarantänebaracke, einer Spitalsbaracke, einem Feuerwehrzeughaus, einer Kirche und mit einem Gasthaus. Insgesamt wurden rund 109 Objekte errichtet. Im Sommer 1916 war das Flüchtlingslager in Betrieb und beherbergte im September 1916 bereits 2.000 Flüchtlinge aus Ostgalizien und der Bukowina. Eine große Gefahr für die Flüchtlinge ging von Krankheiten, hier vor allem vom Flecktyphus, aus. Die Mortalität im Lager dürfte (wie generell in der Bevölkerung der Monarchie im Verlaufe des Krieges) sehr hoch gewesen sein, was die Evidenz der Totenscheine der verstorbenen Orthodoxen erahnen lässt, die wir in unserem Projekt im Detail erforschen (s. u.). </p>
<p>Aufgelassen wurde das Flüchtlingslager Oberhollabrunn, das zur Zeit der stärksten Belegung über 4.000 Flüchtlinge beherbergte, schließlich Ende April 1918 und wurde mit der Ausrufung der Ersten Republik am 12. November 1918 einer neuen Verwendung zugeführt. Ab Dezember 1918 wurden Kinder zwischen 14 und 16 Jahren seitens der Stadt Wien zwecks Erholung in den verlassenen Gebäuden untergebracht, womit ein neues Kapitel der Geschichte begann. </p>

<p>Unser Forschungsprojekt basiert auf unveröffentlichten Beständen des Archivs der griechisch-orthodoxen Kirchengemeinde zur Heiligen Dreifaltigkeit in der Metropolis von Austria (Fleischmarkt 13, 1010 Wien), die gleichzeitig Trägerin des vorliegenden Projekts ist. Wir haben zwei Gruppen von Archivalien identifiziert, auf denen unser sozialgeschichtlicher Forschungsansatz fußt. Der erste, kleinere Bestand sind Ehe-, Tauf- und Sterbematriken der orthodoxen Flüchtlinge aus Oberhollabrunn.  Eine ungleich größere Gruppe bilden 343 Totenbeschaubefunde zu den orthodoxen Flüchtlingen. Von besonderer biographischer und sozialgeschichtlicher Bedeutung sind die Totenbeschaubefunde. </p>
<p>Die obenerwähnten Archivalien werden durch die wissenschaftlichen MitarbeiterInnen, Frau Sandra Wabnitz, BA und Frau Itana Ćupić, BSc, aufgearbeitet, erschlossen und in eine OpenAtlas Datenbank (<a href="https://openatlas.eu/" target="_blank">https://openatlas.eu/</a>) eingegeben werden. All diese Daten werden wir danach im digitalen Geoportal der Geschichte der Orthodoxen in Österreich frei zugänglich und abrufbar machen. Dadurch werden wir es ermöglichen, den Lebensweg der orthodoxen Flüchtlinge zu rekonstruieren und mit digitalen kartographischen Mitteln ein Bild ihrer Flucht aus ihren jeweiligen Lebenswelten in eine neue, unbekannte Umgebung nachzuzeichnen.</p>
<p>Dieses Geoportal sowie eine App für Smartphones wird in Zusammenarbeit mit dem Austrian Institute of Technology (AIT; hier Dr. Rainer Simon) verwirklicht werden. </p>

<p>Vergleichen Sie dazu bitte auch folgenden Link des Fördergebers: 
<a href="http://www.zukunftsfonds-austria.at/projektinfo.php?pcode=P19-3804" target="_blank">http://www.zukunftsfonds-austria.at/projektinfo.php?pcode=P19-3804</a> </p>

 """
    }),
    ('Geoportal', {
        'id': '2',
        'image': "ratzenstadtl.jpg",
        'title': 'Ein digitales Geoportal der Geschichte der SerbInnen in Wien (1741-1918)',
        'subtitle': '',
        'number': 'Zukunftsfonds der Republik Österreich P19-3804',
        'duration': '1. Jänner 2018 bis 30. Juni 2019 (18 Monate) ',
        'pi': 'Priv.-Doz. Mag. Dr. Mihailo Popović',
        'members': ['Sandra Wabnitz', 'Itana Ćupić'],
        'institute': ['ABF'],
        'sponsor': ['MA7'],
        'partners': ['AIT'],
        'description': """ <p>Das MA 7-Projekt mit dem Titel „Ein digitales Geoportal der Geschichte der SerbInnen in Wien (1741-1918)“ hatte eine reguläre Laufzeit von 1. Jänner 2018 bis 31. Dezember 2018 und wurde vom Projektleiter Doz. Mag. Dr. Mihailo Popović aufgrund der Fülle der sowohl in Österreich als auch in Serbien gefundenen Archivalien um ein weiteres halbes Jahr (bis 30. Juni 2019) kostenneutral verlängert. Der wissenschaftliche Mitarbeiter des Projektes, Herr Zlatan Stojadinović, BA, hat seine Projektarbeit mit 1. Jänner 2018 aufgenommen und auch in der kostenneutralen Phase ununterbrochen ehrenamtlich weitergeführt. In der ersten Hälfte des Jahres 2018 hat er eine Liste der Wiener SerbInnen im Zeitraum 1741 bis 1918 zusammengestellt, die damals 250 Personen umfaßte. Diese Liste gliedert sich in folgende Berufsgruppen: Offiziere, Schriftsteller und Dichter, Händler, Zeitungsherausgeber und Journalisten, Herrscher (Fürsten und Könige Serbiens), Künstler und Wissenschaftler. Mit Projektende befinden sich 280 Personen und 241 Orte in der OpenAtlas Datenbank des Projektes (Backend).</p>
<p>Diese Daten wurden in großer Detailarbeit von Herrn Stojadinović, den ehrenamtlichen Mitarbeiterinnen Marijana Kokanović Marković, PhD und Mag.a. Vera Merkel-Tiefenthaler sowie vom Projektleiter anhand von Sekundärliteratur und durchwegs unveröffentlichten Archivalien aus Archiven in Österreich und Serbien recherchiert, gesammelt und ausgewertet (hier aus folgenden Archiven: Allgemeines Verwaltungsarchiv – Finanz- und Hofkammerarchiv, Wien; Haus-, Hof- und Staatsarchiv, Wien; Kriegsarchiv, Wien; Wiener Stadt- und Landesarchiv; Archiv der Universität Wien; Universitätsarchiv der Akademie der bildenden Künste, Wien; Archiv der Gesellschaft der Musikfreunde in Wien; Archiv der Universität für Musik und darstellende Kunst Wien; Archiv der Technischen Universität Wien; Archiv der serbisch-orthodoxen Kirchengemeinde zum Heiligen Sava, Wien; Archiv der griechisch-orthodoxen Kirchengemeinde zur Heiligen Dreifaltigkeit, Wien; Österreichische Nationalbibliothek, Wien; Niederösterreichisches Landesarchiv, Sankt Pölten; Narodna Biblioteka Srbije, Belgrad; Muzej grada Beograda, Belgrad; Biblioteka Matice Srpske, Novi Sad sowie Recherche in den online Matriken der Votivkirche, St. Ulrich, Ev. Diözese A.B., St. Stephan, St. Rochus, St. Elisabeth, Pfarre Schotten und St. Maria Rotunda). </p>
<p>Die daraus gewonnenen biographischen Abrisse wurden in englischer Sprache in die OpenAtlas Datenbank des Projekts (Backend) in minutiöser Arbeit eingegeben, um die internationale Nutzung der Projektergebnisse zu erleichtern. Des weiteren wurden umfassende Bilddaten in die Datenbank integriert: einerseits Porträts, d. h. Gemälde, Zeichnungen und Photographien der historischen Persönlichkeiten, andererseits Aufnahmen von Gebäuden in Wien (auch von Gedenktafeln und Denkmälern), in denen sie gelebt oder gewirkt haben. Bei den Aufnahmen von Gebäuden wurde strikt darauf geachtet, daß diese öffentlichen Raum zeigen, damit die Bestimmungen der Datenschutzgrundverordnung nicht verletzt werden. Umfassende Bilddaten (vor allem Porträts, aber auch Scans alter Drucke und Bücher) wurden dem Projekt nach gezielten Verhandlungen unentgeltlich von Institutionen der Republik Serbien (hier Narodna Biblioteka Srbije, Belgrad; Muzej grada Beograda, Belgrad; Biblioteka Matice Srpske, Novi Sad) zur Verfügung gestellt, wodurch grenzüberschreitende wissenschaftliche Synergien entstanden sind.</p>
<p>Das Austrian Institute of Technology (AIT) in Wien, hier Dr. Rainer Simon, hat ein Geoportal (Web-Application) als Frontend für das Projekt entwickelt, in das alle obenerwähnten Daten eingespielt wurden. Damit können die NutzerInnen sowohl Orte auf einer interaktiven Karte als auch die jeweiligen historischen Persönlichkeiten aufrufen und sich auf Spurensuche – sei es digital oder tatsächlich im Wiener Stadtbild – machen.</p>
<p>Das Projekt ist seit Anbeginn mit einer eigenen Homepage online (<a href="https://orthodoxes-wien.oeaw.ac.at/" target="_blank">https://orthodoxes-wien.oeaw.ac.at/</a>). Es wurde Mitte November 2019 im Gemeindesaal der rumänisch-orthodoxen Kirche „Zur hl. Auferstehung und hl. Ap. Andreas“ (Simmeringer Hauptstraße 161, 1110 Wien) offiziell lanciert und ist seitdem online frei zugänglich. </p>
"""
    }),
])


@app.route('/projekte')
def projekte():
    return render_template('projekte.html', projects=projects_)

@app.route('/projekte/<projekt>')
def projekt_detail(projekt):
    return render_template('projekt_details.html', projekt=projects_[projekt])