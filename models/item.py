from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    productArea = db.Column(db.String(80))
    date = db.Column(db.String(80))
    priority = db.Column(db.Integer)


    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, description, productArea, date, priority, store_id):
        self.name = name
        self.description = description
        self.productArea = productArea
        self.date = date
        self.priority = priority
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'description': self.description,'productArea': self.productArea, 'date': self.date, 'priority': self.priority}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name = name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
   