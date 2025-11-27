# LiFi overzicht project code
In dit READ ME documentje staat zo overzichtelijk mogelijk wat er in de code in brede banen gebeurd. Hierop volgend zal er nog een stukje geschreven staan over hoe met behulp van deze code, bestandjes en de juiste hardware de setup kan worden gerecreëerd.

## Documenten type en doel
Er zijn vier zo genaamde source documenten. In andere woorden de vier documentjes die alle door ons geprogrammeerde code uitvoeren:

- boord_gebruiker.cpp
- bits_naar_string.py
- hamming_code.py
- update_interface.py.

Aan de .cpp en .py kan je zien dat enkel boord_gebruiker.cpp in C++ is gecodeerd terwijl de andere documenten in Python zijn geschreven.

Het boord_gebruiker.cpp heeft als doel om het Wemos d1 mini bord te activeren waarna het lichtsignalen oppikt en ook lichtsignalen kan zenden wanneer deze hier de data voor toegestuurd krijgt uit het update_intergace.py bestand.

bits_naar_string.py heeft één van de twee ondersteunende rollen die het overzichtelijk houdt. Dit document bevat dictionary geralateerde functies en de bijpassende dictionaries die uit de update_interface.py kunnen worden aangeroepen. 

De andere ondersteunende rol gaat naar hamming_code.py die door zowel bits_naar_string als door de update_interface wordt aangeroepen. De hamming code zorgt er voor dat alle bits nog een keer worden gecontroleerd.

Ten slotte is de update_interface.py bestand als het ware het brein in deze virtuele opstelling. Dit is dan ook het documentje dat de eerste schakel tussen de gebruiker en de rest van de code vormt.

## Bestand gebruiksinstructies
Om de interface op te roepen zal je allereerst de hardware goed moeten afstellen en scherpstellen. Om dit te doen heb je echter een aantal extensies die moeten worden gedownload. Alle extensies die ik momenteel gedownload heb zijn als volgt: GitHub Codespaces, Pylance, Arduino, C/C++, C/C++ Extension Pack, C/C++ Themes, CMake Tools, Gitlens-Git supercharged, Live Share, PlatformIO IDE, Python, Python Debugger, Python Environments, SQLite3 Editor en tot slot vscode-pdf. Wanneer je de benodigde van deze lijst hebt gedownload kan je beginnen aan het opstarten van de juiste software.

Dit doe je door in het boord_gebruiker.cpp documentje in github op het knopje in de vorm van de pijl naar rechts onderaan je werkbalk te klikken. Je weet dat dit het juiste knopje is wanneer je er overheen hovert met je muis en er een klein displaytje oppopt waarop 'PlatformIO: Upload' op staat. Als het goed is begint je laptop nu code te runnen in een nieuwe terminal, dit is voltooid en goed gegaan zodra je hierin de boodschap [SUCCESS] ontvangt.

Nadat je dit hebt gedaan behoor je naar het update_interface.py documentje te gaan zolang je het zenden van lichtstralen wil nabootsen. In dit document moet je naar het stukje na de hashtag kijken waar "# Pas dit aan naar jouw seriële poort:" staat en bij de regel daaronder de hashtag verwijderen en de seriële poort invullen waar jouw Wemos d1 mini op aangesloten staat. 

Wanneer dit gelukt is hoef je enkel nog op het checkje, het symbool links van de pijl die je hiervoor moest klikken, te klikken en daarmee zou het interface tevoorschijn moeten komen waarna je berichten kan typen, ontvangen en versturen mits de hardware juist aanwezig is.
