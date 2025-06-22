from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.kamar import Kamar
from models import db

kamar_bp = Blueprint('kamar', __name__, url_prefix='/kamar')

@kamar_bp.route('/')
def kamar_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    kamars = Kamar.query.all()
    return render_template('kamar_list.html', kamars=kamars)

@kamar_bp.route('/add', methods=['GET', 'POST'])
def kamar_add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        nama = request.form['nama']
        tipe = request.form['tipe']
        harga = request.form['harga']
        kapasitas = request.form['kapasitas']
        fasilitas = request.form['fasilitas']
        k = Kamar(nama=nama, tipe=tipe, harga=harga, kapasitas=kapasitas, fasilitas=fasilitas)
        db.session.add(k)
        db.session.commit()
        flash('Kamar berhasil ditambahkan!', 'success')
        return redirect(url_for('kamar.kamar_list'))
    return render_template('kamar_form.html', form_title='Tambah Kamar', kamar=None)

@kamar_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def kamar_edit(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    kamar = Kamar.query.get_or_404(id)
    if request.method == "POST":
        kamar.nama = request.form['nama']
        kamar.tipe = request.form['tipe']
        kamar.harga = request.form['harga']
        kamar.kapasitas = request.form['kapasitas']
        kamar.fasilitas = request.form['fasilitas']
        db.session.commit()
        flash('Kamar berhasil diubah!', 'success')
        return redirect(url_for('kamar.kamar_list'))
    return render_template('kamar_form.html', form_title='Edit Kamar', kamar=kamar)

@kamar_bp.route('/detail/<int:id>')
def kamar_detail(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    kamar = Kamar.query.get_or_404(id)
    return render_template('kamar_detail.html', kamar=kamar)

@kamar_bp.route('/delete/<int:id>', methods=['POST'])
def kamar_delete(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    kamar = Kamar.query.get_or_404(id)
    db.session.delete(kamar)
    db.session.commit()
    flash('Kamar berhasil dihapus!', 'success')
    return redirect(url_for('kamar.kamar_list'))