from extensions import db


class Comment(db.Model):
    """Data model for comments of article"""

    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    create_at = db.Column(db.DateTime())
    content = db.Column(db.Text())
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
