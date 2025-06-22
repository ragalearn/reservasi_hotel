from models import db

class Kamar(db.Model):
    __tablename__ = 'kamar'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tipe = db.Column(db.String(50), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    kapasitas = db.Column(db.Integer, nullable=False)
    fasilitas = db.Column(db.Text, nullable=False)
    # relasi ke reservasi, referensi class sebagai string
    reservasis = db.relationship('Reservasi', backref='kamar', lazy=True)