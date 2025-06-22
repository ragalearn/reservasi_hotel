from flask import Blueprint, render_template, session, redirect, url_for
from models.tamu import Tamu
from models.kamar import Kamar
from models.reservasi import Reservasi
from datetime import date
from sqlalchemy import extract, func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Statistik dasar
    total_tamu = Tamu.query.count()
    total_kamar = Kamar.query.count()
    total_reservasi = Reservasi.query.count()
    kamar_tersedia = Kamar.query.filter_by(status='Tersedia').count() if hasattr(Kamar, 'status') else total_kamar

    # Data chart: Jumlah reservasi per bulan di tahun ini
    tahun_ini = date.today().year
    chart_data = []
    for bulan in range(1, 13):
        jml = Reservasi.query.filter(
            extract('year', Reservasi.check_in) == tahun_ini,
            extract('month', Reservasi.check_in) == bulan
        ).count()
        chart_data.append(jml)

    # Pemberitahuan dinamis (bisa diambil dari reservasi terbaru, status kamar, dll)
    pemberitahuan = []
    # Contoh: 5 kamar perlu pembersihan
    kamar_perlu_pembersihan = Kamar.query.filter_by(status='Perlu Pembersihan').count() if hasattr(Kamar, 'status') else 0
    if kamar_perlu_pembersihan > 0:
        pemberitahuan.append({
            'pesan': f"{kamar_perlu_pembersihan} kamar perlu pembersihan",
            'waktu': "1 jam lalu",
            'icon': "fas fa-bed text-warning"
        })
    # Contoh: reservasi pending
    reservasi_pending = Reservasi.query.filter_by(status='Pending').count() if hasattr(Reservasi, 'status') else 0
    if reservasi_pending > 0:
        pemberitahuan.append({
            'pesan': f"{reservasi_pending} reservasi pending",
            'waktu': "2 jam lalu",
            'icon': "fas fa-user-clock text-info"
        })
    # Contoh: check-in hari ini
    checkin_hari_ini = Reservasi.query.filter(Reservasi.check_in == date.today()).count()
    if checkin_hari_ini > 0:
        pemberitahuan.append({
            'pesan': f"{checkin_hari_ini} check-in hari ini",
            'waktu': "Hari ini",
            'icon': "fas fa-calendar-day text-success"
        })
    # Contoh: check-out hari ini
    checkout_hari_ini = Reservasi.query.filter(Reservasi.check_out == date.today()).count()
    if checkout_hari_ini > 0:
        pemberitahuan.append({
            'pesan': f"{checkout_hari_ini} check-out hari ini",
            'waktu': "Hari ini",
            'icon': "fas fa-calendar-times text-danger"
        })

    # Tanggal hari ini (opsional, JS tetap akan overwrite)
    tanggal_hari_ini = date.today().strftime("%A, %d %B %Y")

    return render_template(
        'dashboard.html',
        total_tamu=total_tamu,
        total_kamar=total_kamar,
        total_reservasi=total_reservasi,
        kamar_tersedia=kamar_tersedia,
        chart_data=chart_data,
        pemberitahuan=pemberitahuan,
        tanggal_hari_ini=tanggal_hari_ini
    )