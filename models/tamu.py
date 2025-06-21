from models import db

class Tamu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    telepon = db.Column(db.String(20))
    reservasis = db.relationship('Reservasi', backref='tamu', lazy=True)