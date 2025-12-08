### Yksikkötesti raportti

Tiedostoja on 2, joita pitää yksikkötestata:

- citation_repository_test.py
- validate_citation_test.py

## citation_repository_test.py

Yksikkötestit testaavat citation_repository-tiedoston toimivuutta. Tiedosto hoitaa viitteiden sql-kyselyt, sekä tietokannan muokkaamista. Testit tehdään käynnistämällä sovelluksen ja muodostamalla uuden tietokannan jonka jälkeen haetaan, lisätään tai päivitetään tietokantaa.

## validate_citation_test.py

Yksikkötestit testaavat syötteet viiteiden tietokantaan. Yksikkötestit tarkistavat, että vialliset viitteiden syötteet ei lisätä tietokantaan. Syötteitä tarkastetaan util-tiedoston 'validate_citation'-funktion sekä UserInputError-luokan avulla.
