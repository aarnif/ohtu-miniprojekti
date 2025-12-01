from sqlalchemy import text
from config import db
from entities.citation import Citation


def get_citations(query, sort):
    if not sort:
        sort = "title"

    if query:
        search_term = query

        if search_term.startswith("https://doi.org/"):
            search_term = search_term.replace("https://doi.org/", "")
        elif search_term.startswith("http://doi.org/"):
            search_term = search_term.replace("http://doi.org/", "")

        result = db.session.execute(text(
            "SELECT id, title, author, publisher, year, citation_type, doi FROM citations "
            f"WHERE title ILIKE :query \
            OR publisher ILIKE :query \
            OR author ILIKE :query \
            OR doi ILIKE :query \
            ORDER BY {sort}"),
            {"query": f"%{search_term}%"})

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


def delete_citation(citation_id):
    sql = text("DELETE FROM citations WHERE id = :citation_id")
    db.session.execute(sql, {"citation_id": citation_id})
    db.session.commit()


def edit_citation(citation_id, title, author, publisher, year, citation_type, doi):
    sql = text(
        "UPDATE citations SET title = :title, author = :author, "
        "publisher = :publisher, year = :year, citation_type = :citation_type, doi = :doi WHERE id = :citation_id")
    db.session.execute(
        sql, {"title": title, "author": author, "publisher": publisher, "year": year,
              "citation_id": citation_id, "citation_type": citation_type, "doi": doi})
    db.session.commit()


def get_citation_by_id(citation_id):
    sql = text(
        "SELECT id, title, author, publisher, year, citation_type, doi FROM citations WHERE id = :citation_id")
    result = db.session.execute(sql, {"citation_id": citation_id})
    citation = result.fetchone()
    if citation:
        return Citation(citation[0], citation[1], citation[2], citation[3],
                        citation[4], citation[5], citation[6])
    return None
