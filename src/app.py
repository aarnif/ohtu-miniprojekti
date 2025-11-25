from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.citation_repository import get_citations, create_citation
from config import app, test_env
from util import validate_citation, UserInputError
from bibtex_generator import create_bibtex


@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", citations=citations)


@app.route("/new_citation")
def new_citation():
    return render_template("new_citation.html")


@app.route("/create_citation", methods=["POST"])
def citation_creation():
    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    year = request.form.get("year")

    try:
        validate_citation(title, author, publisher, year)
        create_citation(title, author, publisher, year)
        return redirect("/")
    except UserInputError as error:
        flash(str(error))
        return redirect("/new_citation")


@app.route("/download_bibtex_file")
def download_bibtex_file():
    bibtex_content = create_bibtex()
    
    return Response(
        bibtex_content,
        headers={"Content-Disposition": "attachment;filename=exported_citations.bib"}
    )


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
