## Sovelluksen kuvaus

Sovelluksessa pystyy lisätä viittauksia ja nähdä ne tiivistettynä etusivulla.

## Ohtu-backlog

[Ohtu-backlog](https://docs.google.com/spreadsheets/d/1oTP5Rjgg2C-FqnABW5s4XA7-_cJuDUs4J3HnxKMaeN0/edit?gid=1#gid=1)

## Ohtu-raportti

[Ohtu-raportti](https://github.com/aarnif/ohtu-miniprojekti/blob/main/misc/raportti.pdf)

## Definition of done

Koodi toimii: Sovellus ja uusi ominaisuus toimii kaikkien user storyn hyväksymiskriteerien mukaisesti.

Koodin testaus: Koodi on testattu vähintään manuaalisesti.

Koodin siisteys: Pylint menee läpi ilman virheitä ja koodi on muotoiltu autopep8:lla. Lisäksi koodi on toisen tiimiläisen läpikäymää.

## Sovelluksen linkki

https://ohtu-miniprojekti.onrender.com/

## Sovelluksen yksikkötestien raportti

https://github.com/aarnif/ohtu-miniprojekti/blob/main/src/tests/unittest_report.md

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

Sovelluksen testikattavuus:

```
poetry run invoke coverage-report
```

Sovelluksen järjestelmätestit:

```
poetry run invoke test-e2e
```
