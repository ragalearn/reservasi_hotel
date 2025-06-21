from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.kamar import Kamar
from models import db

kamar_bp = Blueprint('kamar', __name__, url_prefix='/kamar')

@kamar_bp.route('/', methods=['GET'])
def kamar_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    kamars = Kamar.query.all()
    return render_template('kamar.html', kamars=kamars)

@kamar_bp.route('/add', methods=['POST'])
def kamar_add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    nama = request.form['nama'].strip()
    tipe = request.form['tipe'].strip()
    harga = request.form['harga']
    # Validasi lebih lanjut
    error = None
    if not nama:
        error = 'Nama kamar wajib diisi!'
    elif not tipe:
        error = 'Tipe kamar wajib diisi!'
    elif not harga or not harga.isdigit() or int(harga) <= 0:
        error = 'Harga harus berupa angka positif!'
    if error:
        flash(error, 'danger')
        return redirect(url_for('kamar.kamar_list'))
    k = Kamar(nama=nama, tipe=tipe, harga=int(harga))
    db.session.add(k)
    db.session.commit()
    flash('Kamar berhasil ditambahkan!', 'success')
    return redirect(url_for('kamar.kamar_list'))

@kamar_bp.route('/edit/<int:id>', methods=['POST'])
def kamar_edit(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    k = Kamar.query.get_or_404(id)
    nama = request.form['nama'].strip()
    tipe = request.form['tipe'].strip()
    harga = request.form['harga']
    # Validasi lebih lanjut
    error = None
    if not nama:
        error = 'Nama kamar wajib diisi!'
    elif not tipe:
        error = 'Tipe kamar wajib diisi!'
    elif not harga or not harga.isdigit() or int(harga) <= 0:
        error = 'Harga harus berupa angka positif!'
    if error:
        flash(error, 'danger')
        return redirect(url_for('kamar.kamar_list'))
    k.nama = nama
    k.tipe = tipe
    k.harga = int(harga)
    db.session.commit()
    flash('Kamar berhasil diubah!', 'success')
    return redirect(url_for('kamar.kamar_list'))

@kamar_bp.route('/delete/<int:id>', methods=['POST'])
def kamar_delete(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    k = Kamar.query.get_or_404(id)
    db.session.delete(k)
    db.session.commit()
    flash('Kamar berhasil dihapus!', 'success')
    return redirect(url_for('kamar.kamar_list'))