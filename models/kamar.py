from models import db
# Penting: lakukan import Review setelah class Review sudah dibuat di models/review.py
from models.review import Review

class Kamar(db.Model):
    __tablename__ = 'kamar'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tipe = db.Column(db.String(50), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    kapasitas = db.Column(db.Integer, nullable=False)
    fasilitas = db.Column(db.String(255), nullable=True)
    # relasi ke review
    reviews = db.relationship('Review', back_populates='kamar', cascade="all, delete-orphan")