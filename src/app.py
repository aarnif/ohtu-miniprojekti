from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_todos, create_todo, set_done
from repositories.citation_repository import get_citations, create_citation
from config import app, test_env
from util import validate_todo, validate_citation

@app.route("/")
def index():
    todos = get_todos()
    unfinished = len([todo for todo in todos if not todo.done])
    citations = get_citations()
    return render_template("index.html", todos=todos, unfinished=unfinished, citations=citations)

@app.route("/new_todo")
def new():
    return render_template("new_todo.html")

@app.route("/new_citation")
def new_citation():
    return render_template("new_citation.html")

@app.route("/create_todo", methods=["POST"])
def todo_creation():
    content = request.form.get("content")

    try:
        validate_todo(content)
        create_todo(content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_todo")
    
@app.route("/create_citation", methods=["POST"])
def citation_creation():
    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    year = request.form.get("year")

    try:
        validate_citation(author, title, publisher, year)
        create_citation(author, title, publisher, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_citation")

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
