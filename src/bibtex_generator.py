def create_bibtex(citations):
    if not citations:
        return ""

    bibtex_content = ""

    for citation in citations:
        # print(citation)
        # Luodaan Bibtexin citekey (kirjoittajan sukunimi + vuosi)
        author_key = citation.author.split()[-1]
        year_key = citation.year
        citekey = f"{author_key}{year_key}"

        # Formatoidaan bibtex entry
        # Huom !! Olettaa suoraan että kyseessä on kirja (@Book)
        # -> myöhemmin kun lisätään muita tyyppejä, tämä pitää vaihtaa muuttujaksi
        bibtex_citation = f"""@Book{{{citekey},
        author = {{{citation.author}}},
        title = {{{citation.title}}},
        publisher = {{{citation.publisher}}},
        year = {{{citation.year}}}
}}

"""
        bibtex_content += bibtex_citation

    return bibtex_content
