from sqlalchemy import text
from config import db
from entities.tag import Tag


def add_tag_to_citation(citation_id, tag_name):
    tag_result = db.session.execute(
        text("SELECT id FROM tags WHERE name = :name"), {"name": tag_name})
    tag = tag_result.fetchone()

    if not tag:
        tag_result = db.session.execute(
            text("INSERT INTO tags (name) VALUES (:name) RETURNING id"),
            {"name": tag_name})
        db.session.commit()
        tag = tag_result.fetchone()

    tag_id = tag[0]

    tag_existing = db.session.execute(
        text("SELECT 1 FROM citation_tags WHERE citation_id = :citation_id AND tag_id = :tag_id"),
        {"citation_id": citation_id, "tag_id": tag_id}
    ).fetchone()

    if not tag_existing:
        db.session.execute(
            text(
                "INSERT INTO citation_tags (citation_id, tag_id) VALUES (:citation_id, :tag_id)"),
            {"citation_id": citation_id, "tag_id": tag_id}
        )
        db.session.commit()


def remove_tag_from_citation(citation_id, tag_id):
    db.session.execute(
        text("DELETE FROM citation_tags WHERE citation_id = :citation_id AND tag_id = :tag_id"),
        {"citation_id": citation_id, "tag_id": tag_id}
    )
    db.session.commit()


def get_citation_tags(citation_id):
    result = db.session.execute(
        text("SELECT t.id, t.name FROM tags t INNER JOIN citation_tags ct ON t.id = ct.tag_id "
             "WHERE ct.citation_id = :citation_id ORDER BY t.name"),
        {"citation_id": citation_id}
    )
    return [Tag(row[0], row[1]) for row in result.fetchall()]


def get_all_tags():
    result = db.session.execute(
        text("SELECT id, name FROM tags ORDER BY name"))
    return [Tag(row[0], row[1]) for row in result.fetchall()]
