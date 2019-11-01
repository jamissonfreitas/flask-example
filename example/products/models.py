from config import db
from safrs import SAFRSBase


# Map model to db table
class Product(SAFRSBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Product %r><product   %r>' % (self.name)

    @property
    def serialize(self):
        return {
            'description': self.description,
            'name': self.name,
            'id': self.id,
        }
