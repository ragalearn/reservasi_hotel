from models import db

class Reservasi(db.Model):
    __tablename__ = 'reservasi'
    id = db.Column(db.Integer, primary_key=True)
    tamu_id = db.Column(db.Integer, db.ForeignKey('tamu.id'), nullable=False)
    kamar_id = db.Column(db.Integer, db.ForeignKey('kamar.id'), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    total_harga = db.Column(db.Integer, nullable=False)