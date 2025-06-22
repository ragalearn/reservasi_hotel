from models import db

class Tamu(db.Model):
    __tablename__ = 'tamu'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200), nullable=True)
    telepon = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    # relasi ke reservasi, referensi class sebagai string
    reservasis = db.relationship('Reservasi', backref='tamu', lazy=True)