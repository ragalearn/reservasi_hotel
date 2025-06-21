from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.tamu import Tamu
from models import db

tamu_bp = Blueprint('tamu', __name__, url_prefix='/tamu')

@tamu_bp.route('/', methods=['GET', 'POST'])
def tamu_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        nama = request.form['nama']
        email = request.form['email']
        telepon = request.form['telepon']
        t = Tamu(nama=nama, email=email, telepon=telepon)
        db.session.add(t)
        db.session.commit()
        flash('Tamu berhasil ditambahkan!', 'success')
    tamus = Tamu.query.all()
    return render_template('tamu.html', tamus=tamus)