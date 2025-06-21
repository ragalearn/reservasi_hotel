from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.reservasi import Reservasi
from models.tamu import Tamu
from models.kamar import Kamar
from models import db

reservasi_bp = Blueprint('reservasi', __name__, url_prefix='/reservasi')

@reservasi_bp.route('/', methods=['GET', 'POST'])
def reservasi_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        tamu_id = request.form['tamu_id']
        kamar_id = request.form['kamar_id']
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        r = Reservasi(tamu_id=tamu_id, kamar_id=kamar_id, check_in=check_in, check_out=check_out)
        db.session.add(r)
        db.session.commit()
        flash('Reservasi berhasil ditambahkan!', 'success')
    reservasis = Reservasi.query.all()
    tamus = Tamu.query.all()
    kamars = Kamar.query.all()
    return render_template('reservasi.html', reservasis=reservasis, tamus=tamus, kamars=kamars)