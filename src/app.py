from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.citation_repository import get_citations, get_citation_by_id, create_citation, delete_citation
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
    citation_type = request.form.get("citation_type")
    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    year = request.form.get("year")
    doi = request.form.get("doi")

    try:
        validate_citation(title, author, publisher, year, citation_type)
        create_citation(title, author, publisher, year, citation_type, doi)
        return redirect("/")

    except UserInputError as error:
        flash(str(error))
        return render_template(
            "new_citation.html",
            citation_type=citation_type,
            author=author,
            title=title,
            publisher=publisher,
            year=year,
            doi=doi
        )


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


@app.route("/citations/<int:citation_id>")
def citation_view(citation_id):
    citation = get_citation_by_id(citation_id)
    return render_template("citation.html", citation=citation)


@app.route("/citations/<citation_id>/delete", methods=["POST"])
def delete(citation_id):
    delete_citation(citation_id)
    flash("Citation deleted successfully!", "success")
    return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
