from . import db

class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(800))
    number_of_bedrooms = db.Column(db.Integer)
    number_of_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Float)
    type = db.Column(db.String(40))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))



    def __init__(self, title, description, number_of_bedrooms, number_of_bathrooms, price, type, location, photo):
        self.title = title
        self.description = description
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo

    