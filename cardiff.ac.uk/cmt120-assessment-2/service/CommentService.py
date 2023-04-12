from datetime import datetime

from database import Comment, Article, User
from extensions import db


def add_comments_on_article(author_id: int, comment_content: str, article_id: int) -> bool:
    """
    Create a new comment
    :param author_id: the user id of the author
    :param comment_content: content of comment
    :param article_id: the article id that this comment belongs to
    :return: True if success
    """
    if not db.session.query(Article.query.filter(Article.id == article_id).exists()).scalar():
        return False
    user = User.query.get_or_404(author_id)
    comment = Comment()
    comment.author = user
    comment.author_id = user.id
    comment.create_at = datetime.now()
    comment.content = comment_content
    comment.article_id = article_id
    db.session.add(comment)
    db.session.commit()
    return True


def get_comment_author_id(comment_id: int) -> int:
    comment = Comment.query.get_or_404(comment_id)
    return comment.author_id


def delete_comment(comment_id: int) -> int:
    """
    Delete a comment with id
    :param comment_id: The id of comment
    :return: The article id that this comment belongs to
    """
    comment = Comment.query.get_or_404(comment_id)
    article_id = comment.article_id
    db.session.delete(comment)
    db.session.commit()
    return article_id
