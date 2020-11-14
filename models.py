from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """ Model for pet """

    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """ return the image from the input url or the default image"""
        return self.photo_url or "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"
    

def connect_db(app):
    """Connect this database to provided Flask app.You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)
