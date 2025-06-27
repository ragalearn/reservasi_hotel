# Reservasi Hotel

Aplikasi web ini dirancang untuk mengelola operasional hotel secara efisien, meliputi manajemen tamu, kamar, reservasi dan mampi menampilkan fungsi CRUD (Create, Read, Update, Delete). Dilengkapi dengan antarmuka web intuitif dan API untuk integrasi sistem lain, serta menggunakan database MySQL untuk penyimpanan data yang baik. Program ini merupakan tantangan project UAS (Ujian Akhir Semester).

## Tujuan Proyek

- Memberikan platform digital untuk proses pemesanan kamar hotel.
- Memudahkan pengelolaan data pelanggan dan kamar.
- Menyediakan antarmuka yang mudah digunakan untuk pengguna maupun admin.
- Mendukung pengembangan lebih lanjut untuk fitur-fitur tambahan seperti pembayaran, laporan, dan integrasi dengan sistem lain.

## Fitur Utama

- Pemesanan kamar hotel
- Manajemen data pelanggan
- Manajemen data kamar (jenis, ketersediaan, harga)
- Pencatatan dan riwayat reservasi

## Instalasi

1. **Clone repositori:**
   ```bash
   git clone https://github.com/ragalearn/reservasi_hotel.git
   cd reservasi_hotel
   ```

2. **Buat dan aktifkan virtual environment (opsional, direkomendasikan):**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/MacOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   > *Catatan: Jika file `requirements.txt` tidak tersedia, pastikan Python (minimal versi 3.7) telah terpasang.*

## Penggunaan

1. **Jalankan aplikasi:**
   ```bash
   python main.py
   ```

2. **Ikuti instruksi pada layar untuk melakukan reservasi, melihat data pelanggan, atau mengatur data kamar.**

3. **Data akan tersimpan di file lokal atau database sesuai implementasi.**
