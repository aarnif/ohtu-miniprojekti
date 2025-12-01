from sqlalchemy import text
from config import db
from entities.citation import Citation


def get_citations(query, sort):
    if not sort:
        sort = "title"

    if query:
        result = db.session.execute(text(
            "SELECT id, title, author, publisher, year, citation_type, doi FROM citations "
            f"WHERE title ILIKE :query OR publisher ILIKE :query OR author ILIKE :query ORDER BY {sort}"),
            {"query": f"%{query}%"})

    else:
        result = db.session.execute(
            text(f"SELECT id, title, author, publisher, year, citation_type, doi FROM citations ORDER BY {sort}"))

    citations = result.fetchall()
    return [Citation(citation[0], citation[1], citation[2], citation[3],
                     citation[4], citation[5], citation[6]) for citation in citations]


def create_citation(title, author, publisher, year, citation_type="book", doi=None):
    sql = text(
        "INSERT INTO citations (title, author, publisher, year, citation_type, doi) "
        "VALUES (:title, :author, :publisher, :year, :citation_type, :doi)")
    db.session.execute(
        sql, {"title": title,
              "author": author,
              "publisher": publisher,
              "year": year,
              "citation_type": citation_type,
              "doi": doi})
    db.session.commit()
