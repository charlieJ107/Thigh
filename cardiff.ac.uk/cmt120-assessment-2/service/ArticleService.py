from datetime import datetime

from extensions import db
from database.Article import Article


def load_all_articles() -> list:
    all_articles = Article.query.all()
    return all_articles


def get_article_by_id(article_id: int) -> Article:
    return db.get_or_404(Article, article_id)


def save_article(article: Article) -> bool:
    if not article.content or not article.subject or not article.id:
        return False
    db.session.commit()
    return True


def add_article(subject: str, content: str) -> bool:
    if not content or not subject:
        return False
    article = Article()
    article.create_at = datetime.now()
    article.content = content
    article.subject = subject
    db.session.add(article)
    db.session.commit()
    return True


def delete_article_by_id(article_id: int) -> None:
    article = get_article_by_id(article_id)
    delete_article(article)


def delete_article(article: Article) -> None:
    db.session.delete(article)
