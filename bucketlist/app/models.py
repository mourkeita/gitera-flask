from app import db

class Bucketlist(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, name):
        """initialize with name."""
        self.name = name
        self.lastname = lastname
        self.age = age

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Bucketlist: {}>".format(self.name)

class Personne(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    lastname = db.Column(db.String(100), unique=False)
    age = db.Column(db.Integer, unique=False)

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        return { 'My name is {}'.format(self.name) }


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Personne.query.all()

    def delete_all(self):
        personnes = Personne.query.all()
        for personne in personnes:
            db.session.delete(personne)