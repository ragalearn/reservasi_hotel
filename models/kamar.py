from models import db

class Kamar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(64), nullable=False)
    tipe = db.Column(db.String(32), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    reservasis = db.relationship('Reservasi', backref='kamar', lazy=True)