# LiFi overzicht project code
In dit READ ME documentje staat zo overzichtelijk mogelijk wat er in de code in brede banen gebeurd. Hierop volgend zal er nog een stukje geschreven staan over hoe met behulp van deze code, bestandjes en de juiste hardware de setup kan worden gerecreëerd.

## Documenten type en doel
Er zijn vier zo genaamde source documenten. In andere woorden de vier documentjes die alle door ons geprogrammeerde code uitvoeren:

- WemosD1_code.cpp
- berichten_converter.py
- hamming_code_converter.py
- interface.py.

Aan de .cpp en .py kan je zien dat enkel WemosD1_code.cpp in C++ is gecodeerd terwijl de andere documenten in Python zijn geschreven.

Het WemosD1_code.cpp heeft als doel om het Wemos D1 mini bord te activeren waarna het lichtsignalen oppikt en deze signalen door te sturen naar inteface.py. Ook kan het lichtsignalen verzenden wanneer interface.py een string van bits stuurt naar WemosD1_code.cpp om te verzenden. 

hamming_code_converter.py heeft één van de twee ondersteunende rollen die het overzichtelijk houdt. Dit document zet strings van bits om met behulp van de hamming code om in een versleutelde string met foutcorrectie en het document kan dit ook de andere kant op doen 

De andere ondersteunende rol gaat naar berichten_converter.py die de ingetypte tekst met behulp van de functies uit hamming_code_converter.py omzet in verstuurbare pakketjes. Het kan ook weer pakketje omzetten in tekst. 

Ten slotte is de interface.py bestand als het ware het brein in deze virtuele opstelling. Dit is dan ook het documentje dat de eerste schakel tussen de gebruiker en de rest van de code vormt. Het maakt gebruik van berichten_converter.py om de teksten om te zetten in bits en verstuurt vervolgens de bits naar WemosD1_code.cpp die de string uiteindelijk verzendt. Interface.py doe ditzelfde maar dan omgekeerd als het een pakketje binnengestuurt krijgt van WemosD1_code.cpp en zorgt ervoor dat het berichtje op het beeld verschijnt. 

## Bestand gebruiksinstructies
Om de interface op te roepen zal je allereerst de hardware goed moeten afstellen en scherpstellen. Om dit te doen heb je echter een paar extensies nodig om de code correct uit te voeren. Je hebt de volgende extensies in Visual Studio Code nodig: C/C++, PlatformIO IDE, Python, Python Environments en GitHub Pull Requests. Wanneer je deze allemaal hebt geïnstalleerd kan je beginnen aan het opstarten van de juiste software.

Dit doe je door in het WemosD1_code.cpp documentje in github op het knopje in de vorm van de pijl naar rechts onderaan je werkbalk te klikken. Je weet dat dit het juiste knopje is wanneer je er overheen hovert met je muis en er een klein displaytje oppopt waarop 'PlatformIO: Upload' op staat. Als het goed is begint je laptop nu code te runnen in een nieuwe terminal, dit is voltooid en goed gegaan zodra je hierin de boodschap [SUCCESS] ontvangt.

Nadat je dit hebt gedaan behoor je naar het interface.py documentje te gaan zolang je het zenden van lichtstralen wil nabootsen. In dit document moet je naar het stukje na de hashtag kijken waar "# Pas dit aan naar jouw seriële poort:" staat en bij de regel daaronder de hashtag verwijderen en de seriële poort invullen waar jouw Wemos D1 mini op aangesloten staat. 

Om te zien op welke port de Wemos D1 mini is aangesloten kan je op Mac Os in terminal de command "ls /dev/cu.*" intypen en op Windows kan je in terminal de command "Get-WmiObject Win32_SerialPort" typen.

Wanneer dit gelukt is hoef je enkel nog op het checkje, het symbool links van de pijl die je hiervoor moest klikken, te klikken en daarmee zou het interface tevoorschijn moeten komen waarna je berichten kan typen, ontvangen en versturen mits de hardware juist aanwezig is.
