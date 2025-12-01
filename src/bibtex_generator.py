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

        # Formatoidaan bibtex entry käyttäen citation_type kenttää
        bibtex_type = citation.citation_type.capitalize()
        bibtex_citation = f"""@{bibtex_type}{{{citekey},
        author = {{{citation.author}}},
        title = {{{citation.title}}},
        publisher = {{{citation.publisher}}},
        year = {{{citation.year}}}"""

        if citation.doi:
            bibtex_citation += f""",
        doi = {{{citation.doi}}}"""

        bibtex_citation += "\n}\n\n"
        bibtex_content += bibtex_citation

    return bibtex_content
