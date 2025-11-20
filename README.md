## Sovelluksen kuvaus

Sovelluksessa pystyy lisätä viittauksia ja nähdä ne tiivistettynä etusivulla.

## Ohtu-backlog

[Ohtu-backlog](https://docs.google.com/spreadsheets/d/1oTP5Rjgg2C-FqnABW5s4XA7-_cJuDUs4J3HnxKMaeN0/edit?gid=1#gid=1)


## Definition of done
Sovellus toimii, testit menevät läpi ja koodi on siistiä.

## Sovelluksen linkki

https://ohtu-miniprojekti.onrender.com/

## Sovelluksen asennusohjeet

Kloonaa repositorio:
```
git clone git@github.com:aarnif/ohtu-miniprojekti.git
```

Avaa sovelluksen hakemisto:
```
cd ohtu-miniprojekti
```

Asenna sovelluksen riippuvuudet:
```
poetry install
```

Alusta sovelluksen käyttämä tietokanta:
```
poetry run invoke build
```

Käynnistä sovellus:
```
poetry run invoke start
```

## Testauskomentoja

Sovelluksen yksikkötestit:
```
poetry run invoke test-unit
```

Sovelluksen järjestelmätestit:
```
poetry run invoke test-e2e
```
