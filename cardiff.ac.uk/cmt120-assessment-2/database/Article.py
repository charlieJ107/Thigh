from extensions import db


class Article(db.Model):
    """A data model for each blog, including content and subject"""

    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime())
    subject = db.Column(db.Text())
    content = db.Column(db.Text())
    cover_image_url = db.Column(db.String(256))
    comments = db.relationship("Comment", backref="article")
