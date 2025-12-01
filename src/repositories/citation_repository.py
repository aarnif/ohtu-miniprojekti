from sqlalchemy import text
from config import db
from entities.citation import Citation


def get_citations(query, sort):
    if not sort:
        sort = "title"

    if query:
        result = db.session.execute(text(
            "SELECT id, title, author, publisher, year FROM citations "
            f"WHERE title ILIKE :query OR publisher ILIKE :query OR author ILIKE :query ORDER BY {sort}"),
            {"query": f"%{query}%"})

    else:
        result = db.session.execute(
            text(f"SELECT id, title, author, publisher, year FROM citations ORDER BY {sort}"))

    citations = result.fetchall()
    return [Citation(citation[0], citation[1], citation[2], citation[3], citation[4]) for citation in citations]


def create_citation(title, author, publisher, year):
    sql = text(
        "INSERT INTO citations (title, author, publisher, year) VALUES (:title, :author, :publisher, :year)")
    db.session.execute(
        sql, {"title": title, "author": author, "publisher": publisher, "year": year})
    db.session.commit()


def delete_citation(citation_id):
    sql = text("DELETE FROM citations WHERE id = :citation_id")
    db.session.execute(sql, {"citation_id": citation_id})
    db.session.commit()


def edit_citation(citation_id, title, author, publisher, year):
    sql = text(
        "UPDATE citations SET title = :title, author = :author, " \
        "publisher = :publisher, year = :year WHERE id = :citation_id")
    db.session.execute(
        sql, {"title": title, "author": author, "publisher": publisher, "year": year, "citation_id": citation_id})
    db.session.commit()
