import os
from sqlalchemy import text
from config import db, app
from data import CITATIONS


def reset_db():
    print("Clearing contents from table citations")
    sql = text("DELETE FROM citations")
    db.session.execute(sql)
    db.session.commit()


def populate_db():
    print("Populating database with sample citations")

    sql = text(
        "INSERT INTO citations (author, title, publisher, year, citation_type, doi) "
        "VALUES (:author, :title, :publisher, :year, :citation_type, :doi)"
    )
    db.session.execute(sql, CITATIONS)

    db.session.commit()
    print(f"Added {len(CITATIONS)} citations to the database")


def tables():
    """Returns all table names from the database except those ending with _id_seq"""
    sql = text(
        "SELECT table_name "
        "FROM information_schema.tables "
        "WHERE table_schema = 'public' "
        "AND table_name NOT LIKE '%_id_seq'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]


def enums():
    """Returns all enum type names from the database"""
    sql = text(
        "SELECT typname "
        "FROM pg_type "
        "WHERE typtype = 'e' "
        "AND typnamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'public')"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]


def setup_db():
    """
      Creating the database
      If database tables already exist, those are dropped before the creation
    """
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table}")
            db.session.execute(sql)
        db.session.commit()

    enums_in_db = enums()
    if len(enums_in_db) > 0:
        print(f"Enums exist, dropping: {', '.join(enums_in_db)}")
        for enum in enums_in_db:
            sql = text(f"DROP TYPE {enum}")
            db.session.execute(sql)
        db.session.commit()

    print("Creating database")

    # Read schema from schema.sql file
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        schema_sql = f.read().strip()

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
        populate_db()
