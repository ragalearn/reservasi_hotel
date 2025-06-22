from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models.tamu import Tamu
from models import db

tamu_bp = Blueprint('tamu', __name__, url_prefix='/tamu')

@tamu_bp.route('/')
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
        email = request.form['email']
        telepon = request.form['telepon']
        t = Tamu(nama=nama, email=email, telepon=telepon)
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
        tamu.nama = request.form['nama']
        tamu.email = request.form['email']
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
    db.session.delete(tamu)
    db.session.commit()
    flash('Tamu berhasil dihapus!', 'success')
    return redirect(url_for('tamu.tamu_list'))