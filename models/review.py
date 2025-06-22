from models import db

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    kamar_id = db.Column(db.Integer, db.ForeignKey('kamar.id'), nullable=False)
    nama_reviewer = db.Column(db.String(100), nullable=False)
    komentar = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    tanggal = db.Column(db.Date, nullable=False)

    kamar = db.relationship('Kamar', back_populates='reviews')