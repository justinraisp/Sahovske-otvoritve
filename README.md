
Šahovske otvoritve
=======================

Analiziral bom  1978 šahovskih otvoritev, ki imajo odigranih vsaj 100 profesionalnih partij.
[Chess_openings](https://old.chesstempo.com/chess-openings.html).

Za vsako otvoritev sem zajel:
* ime otvoritve
* število iger
* barvo šahista
* datum zadnje odigrane partije
* povprečen in odigran rating šahista, ki je odigral to otvoritev
* odstotek zmag, remijev in porazev
* poteze in število potez v otvoritvi

Datoteka `zajem.py` vsebuje postopek zajema s spletne strani iz HTML datotek iz mape `otvoritve`. Datoteka `urejanje_podatkov.py` pa vsebuje postopek urejanja podatkov. Podatki, ki jih bom analiziral so pa shranjeni v CSV datoteki v mapi pod imenom `otvoritve`.
 
Delovne hipoteze:
* Ali so si med seboj podobne najuspešnejše in med seboj najmanj uspešne otvoritve?
* Ali obstaja povezava med uspešnostjo in datumom zadnje partije?
* Ali lahko na podlagi povprečnega in odigranega ratinga igralca sklepamo na odstotek zmage?
* Ali so otvoritve belih uspešnejše od otvoritve črnih?
