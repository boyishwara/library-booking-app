# Library Booking App - Automation Tests

Direktori ini berisi script pengujian otomatis (Automation Testing) untuk modul **Create Booking (View Room & Time Rules)** menggunakan **Selenium Webdriver** dan **Locust** (Load Testing).

## Prasyarat (Prerequisites)
1. Python 3.x terinstal di sistem.
2. Library yang dibutuhkan:
   ```bash
   pip install selenium webdriver-manager locust
   ```
3. Browser Google Chrome.
4. Server lokal (XAMPP/Laragon) yang sudah menjalankan project Library Booking App pada `http://localhost`.

---

## 1. Functional Automation Testing (`test_full.py`)

Script ini berfokus pada **Black-Box Functional Testing**. Script ini menguji antarmuka UI dan 13 aturan bisnis (Business Rules) waktu dan role dari proses Create Booking.

### Cara Menjalankan:
```bash
python test_full.py
```

### Makna Hasil (Pass/Fail):
- **PASS**: Sistem berperilaku persis seperti yang diharapkan pada spesifikasi dokumen (IEEE 829). Validasi menolak input yang salah dan menampilkan pesan error UI yang tepat, atau menerima input yang benar.
- **FAIL**: Terdapat anomali. Anomali ini bisa berupa:
  - Validasi berhasil di-_bypass_ (sistem menerima input ilegal).
  - Pesan error yang dimunculkan salah atau tidak sesuai konteks (Misal: masalah di TC-F-13).
  - Sistem mengalami **Crash / Error 500** (Misal: masalah di TC-F-02 saat bypass Role AdminOnly).

---

## 2. Integration Automation Testing (`test_integration.py`)

Script ini berfokus pada pengujian integrasi antar-modul dan _database_ (5 Skenario). Menguji interaksi fitur booking dengan konflik jadwal di database, pengecekan _Library Closure_, dan fitur upload file (surat tugas).

### Cara Menjalankan:
```bash
python test_integration.py
```

### Makna Hasil (Pass/Fail):
- **PASS**: Integrasi data dari Form UI hingga masuk ke Database (sebagai _Draft_ atau ditolak karena bentrok _Verified_) berjalan sempurna. File upload berhasil tersimpan ke sistem _storage_.
- **FAIL**: Terjadi kegagalan komunikasi atau sinkronisasi dengan database. Contoh: draft tidak masuk ke tabel, sistem gagal mendeteksi bentrokan waktu, atau upload file gagal/korup.

---

## 3. Load & Performance Testing (Locust)

Digunakan untuk menguji stabilitas performa sistem jika diakses oleh banyak pengguna (Virtual Users) secara bersamaan (Konkurensi). Locust akan mem-bombardir _endpoint_ `GET /rooms` untuk memastikan halaman merespons dengan cepat.

### Cara Menjalankan:
1. Pastikan server web aktif.
2. Jalankan perintah locust di terminal:
   ```bash
   locust -f locustfile.py --host=http://localhost:8000
   ```
   *(Ganti port `8000` dengan port web server yang sesuai, misal `http://localhost` jika menggunakan port 80 standar).*
3. Buka Dashboard Locust di browser melalui: `http://localhost:8089`
4. Masukkan jumlah pengguna (misal: 100) dan _Spawn Rate_ (misal: 10 user/detik).
5. Klik **Start Swarming**.

### Membaca Hasil Load Test:
- Perhatikan **Response Times (ms)** pada dashboard Locust. Jika rata-rata response time tetap < 500ms meski pengguna mencapai puncaknya, performa sistem sangat baik (**Superior**).
- Jika ada **Failures**, berarti server kewalahan dan memunculkan error _Connection Timeout_ atau _500 Internal Server Error_. Ini pertanda sistem membutuhkan optimasi (misal: penambahan RAM/CPU server atau optimasi Query Database).
