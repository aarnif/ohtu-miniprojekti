from datetime import datetime
from sqlalchemy import text
from config import db
from entities.citation import Citation
from repositories.tag_repository import get_citation_tags


def get_citations(query, sort, citation_type, tags=None):
    if not sort:
        sort = "title"

    params = {}

    if tags:
        tag_placeholders = ", ".join([f":tag_{i}" for i in range(len(tags))])

        for i, tag in enumerate(tags):
            params[f"tag_{i}"] = tag

        sql_query = (f"SELECT DISTINCT c.id, c.title, c.author, c.publisher,"
                     "c.year, c.citation_type, c.doi FROM citations c "
                     "INNER JOIN citation_tags ct ON c.id = ct.citation_id "
                     "INNER JOIN tags t ON ct.tag_id = t.id "
                     f"WHERE t.name IN ({tag_placeholders}) ")
    else:
        sql_query = "SELECT c.id, c.title, c.author, c.publisher, " \
            "c.year, c.citation_type, c.doi FROM citations c WHERE 1=1 "

    if query:
        if query.startswith("https://doi.org/"):
            query = query.replace("https://doi.org/", "")
        elif query.startswith("http://doi.org/"):
            query = query.replace("http://doi.org/", "")

        sql_query += "AND (title ILIKE :q OR author ILIKE :q OR publisher ILIKE :q OR doi ILIKE :q"
        params["q"] = f"%{query}%"

        if query.isdigit():
            year_start = int(query + "0" * (4 - len(query)))
            year_end = int(query + "9" * (4 - len(query)))
            current_year = datetime.now().year
            year_end = min(year_end, current_year)
            sql_query += " OR year BETWEEN :year_start AND :year_end)"
            params["year_start"] = year_start
            params["year_end"] = year_end
        else:
            sql_query += ")"

    if citation_type:
        sql_query += "AND citation_type = :citation_type"
        params["citation_type"] = citation_type

    sql_query += f" ORDER BY {sort}"

    result = db.session.execute(text(sql_query), params)
    citations = result.fetchall()

    return [Citation(citation[0], citation[1], citation[2], citation[3],
                     citation[4], citation[5], citation[6], get_citation_tags(citation[0])) for citation in citations]


def create_citation(title, author, publisher, year, citation_type="book", doi=None):
    sql = text(
        "INSERT INTO citations (title, author, publisher, year, citation_type, doi) "
        "VALUES (:title, :author, :publisher, :year, :citation_type, :doi) RETURNING id")
    result = db.session.execute(
        sql, {"author": author,
              "title": title,
              "publisher": publisher,
              "year": year,
              "citation_type": citation_type,
              "doi": doi})
    db.session.commit()
    return result.fetchone()


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
        tags = get_citation_tags(citation_id)
        return Citation(citation[0], citation[1], citation[2], citation[3], citation[4], citation[5], citation[6], tags)
    return None


def check_if_citation_exists(title, doi=None):
    query = "SELECT id, author, title, publisher, year, citation_type, doi FROM citations WHERE title = :title"
    params = {"title": title}

    if doi:
        query += " OR doi = :doi"
        params["doi"] = doi

    result = db.session.execute(text(query), params)
    citation_result = result.fetchone()
    return citation_result
