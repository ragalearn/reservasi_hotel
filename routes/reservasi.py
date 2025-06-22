from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.reservasi import Reservasi
from models.tamu import Tamu
from models.kamar import Kamar
from models import db

reservasi_bp = Blueprint('reservasi', __name__, url_prefix='/reservasi')

@reservasi_bp.route('/')
def reservasi_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    reservasis = Reservasi.query.all()
    return render_template('reservasi_list.html', reservasis=reservasis)

@reservasi_bp.route('/add', methods=['GET', 'POST'])
def reservasi_add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tamus = Tamu.query.all()
    kamars = Kamar.query.all()
    if request.method == "POST":
        tamu_id = request.form['tamu_id']
        kamar_id = request.form['kamar_id']
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        r = Reservasi(tamu_id=tamu_id, kamar_id=kamar_id, check_in=check_in, check_out=check_out)
        db.session.add(r)
        db.session.commit()
        flash('Reservasi berhasil ditambahkan!', 'success')
        return redirect(url_for('reservasi.reservasi_list'))
    return render_template('reservasi_form.html', form_title='Tambah Reservasi', reservasi=None, tamus=tamus, kamars=kamars)

@reservasi_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def reservasi_edit(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    reservasi = Reservasi.query.get_or_404(id)
    tamus = Tamu.query.all()
    kamars = Kamar.query.all()
    if request.method == "POST":
        reservasi.tamu_id = request.form['tamu_id']
        reservasi.kamar_id = request.form['kamar_id']
        reservasi.check_in = request.form['check_in']
        reservasi.check_out = request.form['check_out']
        db.session.commit()
        flash('Reservasi berhasil diubah!', 'success')
        return redirect(url_for('reservasi.reservasi_list'))
    return render_template('reservasi_form.html', form_title='Edit Reservasi', reservasi=reservasi, tamus=tamus, kamars=kamars)

@reservasi_bp.route('/detail/<int:id>')
def reservasi_detail(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    reservasi = Reservasi.query.get_or_404(id)
    return render_template('reservasi_detail.html', reservasi=reservasi)

@reservasi_bp.route('/delete/<int:id>', methods=['POST'])
def reservasi_delete(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    reservasi = Reservasi.query.get_or_404(id)
    db.session.delete(reservasi)
    db.session.commit()
    flash('Reservasi berhasil dihapus!', 'success')
    return redirect(url_for('reservasi.reservasi_list'))