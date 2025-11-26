from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.citation_repository import get_citations, create_citation, delete_citation
from config import app, test_env
from util import validate_citation, UserInputError
from bibtex_generator import create_bibtex


@app.route("/")
def index():
    query = request.args.get("query", "")
    sort = request.args.get('sort', "")
    citations = get_citations(query, sort)
    return render_template("index.html", citations=citations, query=query, sort=sort)


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
    query = request.args.get("query", "")
    sort = request.args.get('sort', "")
    citations = get_citations(query, sort)
    bibtex_content = create_bibtex(citations)
    return Response(
        bibtex_content,
        headers={"Content-Disposition": "attachment;filename=exported_citations.bib"}
    )

@app.route("/delete_citation/<citation_id>", methods=["POST"])
def delete_citation_route(citation_id):
    delete_citation(citation_id)
    return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
