from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.citation_repository import (
    get_citations,
    create_citation,
    delete_citation,
    edit_citation,
    get_citation_by_id,
    check_if_citation_exists
)
from repositories.tag_repository import get_all_tags, add_tag_to_citation, get_citation_tags, remove_tag_from_citation

from config import app, test_env
from util import validate_citation, UserInputError
from bibtex_generator import create_bibtex
from entities.citation import Citation


@app.route("/")
def index():
    query = request.args.get('query', '')
    sort = request.args.get('sort', '')
    citation_type = request.args.get('citation_type', '')
    tags = request.args.getlist('tags')
    all_tags = get_all_tags()
    selected_tags = []

    if tags:
        selected_tags = tags[:]

    citations = get_citations(query, sort, citation_type, selected_tags)
    return render_template("index.html",
                           citations=citations,
                           query=query,
                           sort=sort,
                           citation_type=citation_type,
                           all_tags=all_tags,
                           selected_tags=selected_tags)


@app.route("/new_citation")
def new():
    all_tags = get_all_tags()
    return render_template("new_citation.html",
                           citation_type="",
                           author="",
                           title="",
                           publisher="",
                           year="",
                           doi="",
                           all_tags=all_tags,
                           selected_tags=[])


@app.route("/create_citation", methods=["POST"])
def citation_adding():
    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    year = request.form.get("year")
    citation_type = request.form.get("citation_type", "book")
    doi = request.form.get("doi")
    tags = request.form.getlist("tags")

    if check_if_citation_exists(title, doi):
        flash("Citation already exists!", "error")
        all_tags = get_all_tags()
        return render_template(
            "new_citation.html",
            citation_type=citation_type,
            author=author,
            title=title,
            publisher=publisher,
            year=year,
            doi=doi,
            all_tags=all_tags,
            selected_tags=tags
        )

    try:
        validate_citation(title, author, publisher, year, citation_type)
        citation = create_citation(
            title, author, publisher, year, citation_type, doi)

        citation_id = citation[0]

        for tag in tags:
            if tag.strip():
                add_tag_to_citation(citation_id, tag.strip())

        flash("Citation added successfully!", "success")
        return redirect("/")
    except UserInputError as error:
        flash(str(error), "error")
        all_tags = get_all_tags()
        return render_template("new_citation.html",
                               citation_type=citation_type,
                               author=author,
                               title=title,
                               publisher=publisher,
                               year=year,
                               doi=doi,
                               all_tags=all_tags,
                               selected_tags=tags)


@app.route("/download_bibtex_file")
def download_bibtex_file():
    try:
        query = request.args.get("query", "")
        sort = request.args.get('sort', "")
        citation_type = request.args.get('citation_type', "")
        citations = get_citations(query, sort, citation_type)
        bibtex_content = create_bibtex(citations)
        return Response(
            bibtex_content,
            headers={
                "Content-Disposition": "attachment;filename=exported_citations.bib"}
        )
    except Exception:  # pylint: disable=broad-except
        flash("Something went wrong, please try again", "error")
        return redirect("/")


@app.route("/citations/<citation_id>")
def citation_view(citation_id):
    try:
        try:
            citation_id_int = int(citation_id)
        except (ValueError, TypeError):
            return render_template("citation_not_found.html"), 404

        citation = get_citation_by_id(citation_id_int)
        if not citation:
            return render_template("citation_not_found.html"), 404
        return render_template("citation.html", citation=citation)
    except Exception:  # pylint: disable=broad-except
        flash("Something went wrong, please try again", "error")
        return redirect("/")


@app.route("/citations/<citation_id>/delete", methods=["POST"])
def delete(citation_id):
    try:
        delete_citation(citation_id)
        flash("Citation deleted successfully!", "success")
        return redirect("/")
    except Exception:  # pylint: disable=broad-except
        flash("Something went wrong, please try again", "error")
        return redirect("/")


@app.route("/citations/<int:citation_id>/edit", methods=["GET", "POST"])
def citation_editing(citation_id):
    if request.method == "GET":
        citation = get_citation_by_id(citation_id)
        if not citation:
            flash("Citation not found", "error")
            return redirect("/")
        all_tags = get_all_tags()
        current_tags = get_citation_tags(citation_id)
        selected_tag_names = [tag.name for tag in current_tags]
        return render_template("edit_citation.html",
                               citation=citation,
                               all_tags=all_tags,
                               selected_tag_names=selected_tag_names)

    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    year = request.form.get("year")
    citation_type = request.form.get("citation_type", "book")
    doi = request.form.get("doi")
    tags = request.form.getlist("tags")

    try:
        validate_citation(title, author, publisher, year, citation_type)
        edit_citation(citation_id, title, author,
                      publisher, year, citation_type, doi)

        current_tags = get_citation_tags(citation_id)

        for tag in current_tags:
            remove_tag_from_citation(citation_id, tag.id)

        for tag in tags:
            if tag.strip():
                add_tag_to_citation(citation_id, tag.strip())

        flash("Citation edited successfully!", "success")
        return redirect(f"/citations/{citation_id}")
    except UserInputError as error:
        flash(str(error), "error")
        citation_with_user_input = Citation(
            citation_id=citation_id,
            title=title,
            author=author,
            publisher=publisher,
            year=year,
            citation_type=citation_type,
            doi=doi
        )
        all_tags = get_all_tags()
        current_tags = get_citation_tags(citation_id)
        selected_tag_names = [tag.name for tag in current_tags]
        return render_template("edit_citation.html",
                               citation=citation_with_user_input,
                               all_tags=all_tags,
                               selected_tags=selected_tag_names)


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})


@app.errorhandler(404)
def page_not_found(_e):
    return render_template("page_not_found.html"), 404
