from flask import Flask, abort
import secrets
from datetime import datetime
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, logout_user, current_user

from database import *
from extensions import db, login_manager
from service import ArticleService, CommentService, UserService


def create_app() -> Flask:
    """
    Factory function to create APP
    :return: A flask app instance
    """
    _app = Flask(__name__)
    _app.config.from_prefixed_env()
    secret = secrets.token_urlsafe(32)
    _app.secret_key = secret
    with _app.app_context():
        register_extension(_app)
    return _app


def register_extension(_app):
    db.init_app(_app)
    # db.drop_all()
    db.create_all()
    login_manager.login_view = 'login'
    login_manager.init_app(_app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


app = create_app()


@app.route("/")
@app.route("/home")
def home():
    """Renders the home page."""
    articles = ArticleService.load_all_articles()
    return render_template(
        "index.html",
        title="Home Page",
        year=datetime.now().year,
        articles=articles,
    )


@app.route("/contact")
def contact():
    """Renders the contact page."""
    return render_template(
        "contact.html",
        title="Contact",
        year=datetime.now().year,
        message="Your contact page.",
    )


@app.route("/about")
def about():
    """Renders the about page."""
    return render_template(
        "about.html",
        title="About",
        year=datetime.now().year,
        message="Your application description page.",
    )


@app.route("/article/<article_id>")
def article(article_id: int):
    article_entity = ArticleService.get_article_by_id(article_id)

    # convert markdown into html
    from markdown import markdown
    from markupsafe import Markup
    formatted_content = Markup(markdown(article_entity.content))

    return render_template(
        "article.html",
        title=article_entity.subject,
        year=datetime.now().year,
        article=article_entity,
        article_content=formatted_content,
    )


@app.route("/new-article", methods=("GET", "POST"))
@login_required
def new_article():
    if request.method == "POST":
        subject = request.form["subject"]
        content = request.form["content"]
        if not ArticleService.add_article(subject, content):
            flash("Content and Subject are required", "danger")
            return redirect(url_for("home"))
        else:
            flash("Successfully saved your new article.", "success")
            return redirect(url_for("home"))
    else:
        # Request is in GET method
        if current_user.id == 1:
            return render_template(
                "edit-article.html",
                title="New Article",
                year=datetime.now().year
            )
        else:
            return abort(403)


@app.route("/edit-article/<article_id>", methods=("GET", "POST"))
@login_required
def edit_article(article_id: int):
    article_entity = ArticleService.get_article_by_id(article_id)
    if request.method == "POST":
        article_entity.subject = request.form["subject"]
        article_entity.content = request.form["content"]
        if not ArticleService.save_article(article_entity):
            flash("Content and Subject are required", "danger")
            return render_template(
                "edit-article.html",
                year=datetime.now().year,
                title="Edit Article",
                subject=article_entity.subject,
                content=article_entity.content
            )
        else:
            flash("Successfully saved your edited article.", "success")
            return redirect(url_for("article", article_id=article_id))
    else:
        # Request is in GET method
        if current_user.id == 1:
            return render_template(
                "edit-article.html",
                year=datetime.now().year,
                title="Edit Article",
                content=article_entity.content,
                subject=article_entity.subject
            )
        else:
            abort(403)


@app.post("/new-comment/<article_id>")
@login_required
def new_comment(article_id: int):
    content = request.form["content"]
    article_id = article_id
    if CommentService.add_comments_on_article(current_user.id, content, article_id):
        flash("Successfully submit your comment on this article", "success")
        return redirect(url_for("article", article_id=article_id))


@app.post("/comment/<comment_id>")
@login_required
def delete_comment(comment_id: int):
    if current_user.id != CommentService.get_comment_author_id(comment_id):
        return abort(403)
    article_id = CommentService.delete_comment(comment_id)
    return redirect(url_for("article", article_id=article_id))


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template("login.html", title="Login", year=datetime.now().year)
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        if UserService.check_user_login(email, password, remember):
            # if the above check passes, the user is successfully logged in
            return redirect(url_for('home'))
        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))  # if the user doesn't exist or password is wrong, reload the page


@app.route("/sign-up", methods=("GET", "POST"))
def signup():
    if request.method == "GET":
        return render_template("sign-up.html", title="Sign Up", year=datetime.now().year)
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        if UserService.add_new_user(name, email, password):
            return redirect(url_for('login'))
        else:
            flash('Email address already exists', "danger")
            return redirect(url_for('signup'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
