from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Reservasi, Kamar, Tamu
from datetime import datetime

reservasi_bp = Blueprint('reservasi', __name__, url_prefix='/reservasi')

@reservasi_bp.route('/')
def reservasi_root():
    # Redirect langsung ke halaman list reservasi
    return redirect(url_for('reservasi.reservasi_list'))

@reservasi_bp.route('/list')
def reservasi_list():
    reservasis = Reservasi.query.all()
    return render_template('reservasi_list.html', reservasis=reservasis)

@reservasi_bp.route('/add', methods=['GET', 'POST'])
def reservasi_add():
    kamars = Kamar.query.all()
    tamus = Tamu.query.all()
    harga_kamar = {str(kamar.id): kamar.harga for kamar in kamars}

    if request.method == 'POST':
        tamu_id = request.form['tamu_id']
        kamar_id = request.form['kamar_id']
        tgl_masuk = datetime.strptime(request.form['tanggal_masuk'], '%Y-%m-%d')
        tgl_keluar = datetime.strptime(request.form['tanggal_keluar'], '%Y-%m-%d')
        kamar = Kamar.query.get(kamar_id)
        lama = (tgl_keluar - tgl_masuk).days
        if lama <= 0:
            flash('Tanggal keluar harus setelah tanggal masuk.', 'danger')
            return render_template(
                'reservasi_form.html',
                form_title="Tambah Reservasi",
                reservasi=None,
                tamus=tamus,
                kamars=kamars,
                harga_kamar=harga_kamar
            )
        total_harga = lama * kamar.harga
        reservasi = Reservasi(
            tamu_id=tamu_id,
            kamar_id=kamar_id,
            check_in=tgl_masuk,
            check_out=tgl_keluar,
            total_harga=total_harga
        )
        db.session.add(reservasi)
        db.session.commit()
        flash('Reservasi berhasil ditambahkan', 'success')
        return redirect(url_for('reservasi.reservasi_list'))
    return render_template(
        'reservasi_form.html',
        form_title="Tambah Reservasi",
        reservasi=None,
        tamus=tamus,
        kamars=kamars,
        harga_kamar=harga_kamar
    )

@reservasi_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def reservasi_edit(id):
    reservasi = Reservasi.query.get_or_404(id)
    kamars = Kamar.query.all()
    tamus = Tamu.query.all()
    harga_kamar = {str(kamar.id): kamar.harga for kamar in kamars}

    if request.method == 'POST':
        reservasi.tamu_id = request.form['tamu_id']
        reservasi.kamar_id = request.form['kamar_id']
        reservasi.check_in = datetime.strptime(request.form['tanggal_masuk'], '%Y-%m-%d')
        reservasi.check_out = datetime.strptime(request.form['tanggal_keluar'], '%Y-%m-%d')
        kamar = Kamar.query.get(reservasi.kamar_id)
        lama = (reservasi.check_out - reservasi.check_in).days
        if lama <= 0:
            flash('Tanggal keluar harus setelah tanggal masuk.', 'danger')
            return render_template(
                'reservasi_form.html',
                form_title="Edit Reservasi",
                reservasi=reservasi,
                tamus=tamus,
                kamars=kamars,
                harga_kamar=harga_kamar
            )
        reservasi.total_harga = lama * kamar.harga
        db.session.commit()
        flash('Reservasi berhasil diubah!', 'success')
        return redirect(url_for('reservasi.reservasi_list'))
    return render_template(
        'reservasi_form.html',
        form_title="Edit Reservasi",
        reservasi=reservasi,
        tamus=tamus,
        kamars=kamars,
        harga_kamar=harga_kamar
    )

@reservasi_bp.route('/delete/<int:id>', methods=['POST'])
def reservasi_delete(id):
    reservasi = Reservasi.query.get_or_404(id)
    db.session.delete(reservasi)
    db.session.commit()
    flash('Reservasi berhasil dihapus!', 'success')
    return redirect(url_for('reservasi.reservasi_list'))