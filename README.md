# Baigiamasis darbas

### Norėdami sužinoti daugiau apie sukurtoje programoje aprašytą funkcionalumą, perskaitykite šį aprašymą:

Ši programa yra viktorinos žaidimas, kuris leidžia vartotojui atsakyti į klausimus apie Lietuvos salas. Žaidimo pagrindinis langas yra sukuriamas naudojant Tkinter biblioteką.

Žaidimas veikia taip:

Sukuriama duomenų bazė, naudojant SQLAlchemy biblioteką. Duomenų bazėje saugomi klausimai ir rezultatai.

Iš duomenų bazės užkraunami klausimai, kurie yra pasirenkami iš viso klausimų sąrašo (numatytas klausimų kiekis gali būti nustatytas naudojant settings modulį).

Pagrindiniame lange atvaizduojamas pirmasis klausimas.

Vartotojas gali pasirinkti vieną iš galimų atsakymų paspaudęs mygtuką.

Paspaudus atsakymo mygtuką, programa patikrina, ar atsakymas teisingas, ir informuoja vartotoją apie rezultatą.

Toliau pateikiamas kitas klausimas iš klausimų sąrašo.

Kai atsakomi visi klausimai, programa atvaizduoja rezultatus ir leidžia vartotojui įvesti savo vardą.

Rezultatas ir vartotojo vardas išsaugomi duomenų bazėje.

Vartotojui pateikiama informacija apie jo rezultatus ir galimybė pradėti žaidimą iš naujo arba išeiti iš programos.

Norint paleisti programą, turite turėti įdiegtą Python programavimo kalbą ir reikiamas bibliotekas. Pirmiausiai turite sukurti duomenų bazes (viktorina.db ir rezultatai.db) naudojant duomenų bazių vadovus. Tada paleiskite programą, vykdydami kodą.

Prieš paleidžiant programą, įsitikinkite, kad turite visus reikalingus failus, tokius kaip viktorina_orm.py ir rezultatai.py, kurie apibrėžia duomenų bazės modelius.

Mėgaukitės žaisdami viktorinos žaidimą ir išbandykite savo žinias apie Lietuvos salas!


