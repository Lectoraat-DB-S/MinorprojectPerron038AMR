De functie van de Raspberry pi’s in dit project is om communicatie tussen de stations en de MiR100 (AMR) mogelijk te maken. Op elk station (blauwe transportbanden) is een Raspberry pi 4b met twee knoppen en een eindeloopschakelaar bevestigd. Op deze manier kan er op een knop gedrukt worden om de MiR100 op te roepen en taken (missies) uit te laten voeren.

Ik heb op mijn laptop met Windows 11 de versies Python 3.11 en PyCharm Community Edition 2023.2.3 gebruikt.
Ook heb ik RPi.GPIO, sleep, requests en json als imports gebruikt (zie codeDemo.py).

Dit filmpje was de rode draad tijdens het opstellen van het programma: https://www.youtube.com/watch?v=AK7R-zIzcuY&list=PLh3_StUm_Ycmrpc119nij8GDNToSjph3e&index=18&t=538s

Hoe de schakeling/bedrading is opgebouwd staat in het reeds gedeelde TCD document.

Opmerkingen:
•	Als er met een ander account wordt ingelogd op de MiR server zal er een ander wachtwoord (“authorization”) gevormd worden, dit moet dan aangepast worden in de code. 
•	De communicatie wordt gedaan aan de hand van het restAPI van de MiR100, er worden requests van de types “get” en “post” verstuurd naar de MiR100 server (lijnen 18, 26, 36). In de post-requests wordt het guid van de specifieke missie vermeld (lijnen 25 en 35).  
•	Als er te snel op een knop wordt gedrukt is het mogelijk dat de request niet verstuurd wordt. 
•	Volgens dit programma moet er afwisselend op de groene en blauwe knop gedrukt worden. De groene knop doet het als de eindeloopschakelaar laag staat, de blauwe knop doet het als de eindeloopschakelaar hoog staat.
•	De Raspberry pi’s moeten op hetzelfde netwerk zitten als de MiR server, dit is het AWL netwerk. De gebruikte Raspberry pi’s (019 en 017) verbinden automatisch met dit netwerk. 
