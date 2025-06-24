from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.tamu import Tamu
from models import db

tamu_bp = Blueprint('tamu', __name__, url_prefix='/tamu')

@tamu_bp.route('/')
def tamu_root():
    return redirect(url_for('tamu.tamu_list'))

@tamu_bp.route('/list')
def tamu_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tamus = Tamu.query.all()
    return render_template('tamu_list.html', tamus=tamus)

@tamu_bp.route('/add', methods=['GET', 'POST'])
def tamu_add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        nama = request.form['nama']
        alamat = request.form['alamat']
        email = request.form['email']
        telepon = request.form['telepon']
        # Cek apakah email sudah terdaftar
        existing = Tamu.query.filter_by(email=email).first()
        if existing:
            flash('Email sudah terdaftar. Gunakan email lain.', 'danger')
            return redirect(url_for('tamu.tamu_add'))
        t = Tamu(nama=nama, alamat=alamat, email=email, telepon=telepon)
        db.session.add(t)
        db.session.commit()
        flash('Tamu berhasil ditambahkan!', 'success')
        return redirect(url_for('tamu.tamu_list'))
    return render_template('tamu_form.html', form_title='Tambah Tamu', tamu=None)

@tamu_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def tamu_edit(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tamu = Tamu.query.get_or_404(id)
    if request.method == "POST":
        # Validasi agar email tetap unik saat diedit
        new_email = request.form['email']
        if new_email != tamu.email:
            existing = Tamu.query.filter_by(email=new_email).first()
            if existing:
                flash('Email sudah terdaftar. Gunakan email lain.', 'danger')
                return redirect(url_for('tamu.tamu_edit', id=id))
        tamu.nama = request.form['nama']
        tamu.alamat = request.form['alamat']
        tamu.email = new_email
        tamu.telepon = request.form['telepon']
        db.session.commit()
        flash('Tamu berhasil diubah!', 'success')
        return redirect(url_for('tamu.tamu_list'))
    return render_template('tamu_form.html', form_title='Edit Tamu', tamu=tamu)

@tamu_bp.route('/detail/<int:id>')
def tamu_detail(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tamu = Tamu.query.get_or_404(id)
    return render_template('tamu_detail.html', tamu=tamu)

@tamu_bp.route('/delete/<int:id>', methods=['POST'])
def tamu_delete(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tamu = Tamu.query.get_or_404(id)
    # Cegah hapus tamu jika masih punya reservasi
    if hasattr(tamu, 'reservasis') and tamu.reservasis and len(tamu.reservasis) > 0:
        flash('Tamu tidak bisa dihapus karena masih punya reservasi.', 'danger')
        return redirect(url_for('tamu.tamu_list'))
    db.session.delete(tamu)
    db.session.commit()
    flash('Tamu berhasil dihapus!', 'success')
    return redirect(url_for('tamu.tamu_list'))