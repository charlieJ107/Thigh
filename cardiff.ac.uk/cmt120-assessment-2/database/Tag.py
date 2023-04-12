from extensions import db


class Tag(db.Model):
    """Data model of tags"""
    __tabelname__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text())


class TagArticle(db.Model):
    """Connection table between Tags and Articles. They are an many-to-many relationship"""
    __tablename__ = "tag_article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
