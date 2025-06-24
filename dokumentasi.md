# Dokumentasi Proyek: Sistem Reservasi Hotel

## Deskripsi Singkat
Repositori ini berisi aplikasi web untuk **reservasi hotel** berbasis Python (menggunakan framework Flask). Sistem ini mendukung pengelolaan data kamar, tamu, reservasi, serta menyediakan dashboard dan REST API sederhana.

---

## Arsitektur & Cara Kerja Program

- **Struktur Utama:**
  - `app.py` adalah entry-point aplikasi Flask. Pada fungsi `create_app()`, Flask diinisialisasi, konfigurasi dan database di-setup, lalu blueprint dari berbagai modul (kamar, tamu, reservasi, dashboard, api) didaftarkan.
  - Model utama: `models/tamu.py`, `models/kamar.py`, `models/reservasi.py`
  - Routing modular: Folder `routes/` berisi file seperti `kamar.py`, `tamu.py`, `reservasi.py`, `dashboard.py`, `api.py`, masing-masing menangani endpoint terkait.
  - Template HTML: Tersimpan di folder `templates/`. Ada template untuk dashboard, list kamar, form reservasi, dsb.

- **Alur Kerja Singkat:**
  1. User membuka aplikasi (biasanya diarahkan ke login).
  2. Setelah login, user melihat dashboard utama.
  3. User dapat melakukan CRUD data kamar, tamu, dan melakukan proses reservasi.
  4. Fitur API (`/api/`) tersedia untuk kebutuhan integrasi atau AJAX (misal: menghitung harga otomatis di form reservasi).
  5. Dashboard menampilkan informasi terkini, statistik dan notifikasi.

---

## Cara Menjalankan Program

### 1. **Clone Repository**
```bash
git clone https://github.com/ragalearn/reservasi_hotel.git
cd reservasi_hotel
```

### 2. **Buat Virtual Environment & Install Dependensi**
```bash
python -m venv venv
source venv/bin/activate  # untuk Linux/Mac
venv\Scripts\activate     # untuk Windows

pip install -r requirements.txt
```

### 3. **Konfigurasi (Opsional)**
Pastikan file konfigurasi (misal, `config.py` atau variabel environment seperti DB URI) sudah sesuai kebutuhan.

### 4. **Inisialisasi Database**
Biasanya dengan perintah seperti berikut (tergantung implementasi):
```bash
flask db upgrade
# atau jika belum ada migrasi:
flask db init
flask db migrate
flask db upgrade
```
Cek dokumentasi di kode/model jika ada perintah lain yang diperlukan.

### 5. **Jalankan Aplikasi**
```bash
flask run
```
Aplikasi bisa diakses melalui `http://localhost:5000`.

---

## Catatan Tambahan

- **Login**: Ada route khusus `/login` dan `/logout`.
- **Dashboard**: Menampilkan info real-time, statistik reservasi per bulan (menggunakan Chart.js di sisi frontend).
- **Notifikasi & Waktu**: Tanggal dan jam tampil real-time (lihat `dashboard.html`).
- **API**: Endpoint seperti `/api/hitung_harga` digunakan oleh frontend (AJAX) untuk fitur interaktif seperti hitung total harga otomatis saat mengisi form reservasi.

---

**Pastikan Python, pip, dan database yang didukung sudah terpasang di sistem Anda.**
Jika ada error terkait dependensi atau migrasi database, cek README, requirements.txt, atau bagian konfigurasi di repo.

---