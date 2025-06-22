from flask import Blueprint, request, jsonify
from models.kamar import Kamar
from datetime import datetime

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/hitung_harga')
def hitung_harga():
    kamar_id = request.args.get('kamar_id', type=int)
    tanggal_masuk = request.args.get('tanggal_masuk')
    tanggal_keluar = request.args.get('tanggal_keluar')
    if not (kamar_id and tanggal_masuk and tanggal_keluar):
        return jsonify(total_harga=0)
    kamar = Kamar.query.get(kamar_id)
    if not kamar:
        return jsonify(total_harga=0)
    # Contoh: harga per malam dari field kamar.harga
    fmt = "%Y-%m-%d"
    tgl_masuk_dt = datetime.strptime(tanggal_masuk, fmt)
    tgl_keluar_dt = datetime.strptime(tanggal_keluar, fmt)
    malam = (tgl_keluar_dt - tgl_masuk_dt).days
    if malam < 1:
        malam = 1
    total_harga = malam * kamar.harga  # Pastikan ada field harga di model Kamar
    return jsonify(total_harga=total_harga)