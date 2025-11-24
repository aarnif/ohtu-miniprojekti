from sqlalchemy import text
from config import db
from entities.citation import Citation


def get_citations():
    result = db.session.execute(
        text("SELECT id, title, author, publisher, year FROM citations"))
    citations = result.fetchall()
    return [Citation(citation[0], citation[1], citation[2], citation[3], citation[4]) for citation in citations]


def create_citation(title, author, publisher, year):
    sql = text(
        "INSERT INTO citations (title, author, publisher, year) VALUES (:title, :author, :publisher, :year)")
    db.session.execute(
        sql, {"title": title, "author": author, "publisher": publisher, "year": year})
    db.session.commit()
