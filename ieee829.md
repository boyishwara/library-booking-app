# Standar Dokumentasi Pengujian IEEE 829

Struktur dokumen yang harus dipenuhi berdasarkan standar IEEE 829, yang dibagi ke dalam 3 fase utama pengujian:

## 1. Fase Persiapan Pengujian (Test Preparation)

Fase ini fokus pada perencanaan dan pendefinisian apa saja yang akan diuji, bagaimana caranya, serta alat apa yang dibutuhkan.

### A. Master Test Plan (MTP) / Rencana Pengujian

Dokumen induk yang menetapkan cakupan, pendekatan, sumber daya, dan jadwal aktivitas pengujian. Poin yang harus dipenuhi:

- **Test Plan Identifier:** ID unik untuk dokumen pengujian.
- **Introduction:** Pengantar dan ringkasan proyek.
- **Test Items:** Objek atau modul perangkat lunak yang akan diuji.
- **Features to be Tested:** Fitur-fitur yang masuk dalam cakupan uji.
- **Features not to be Tested:** Fitur yang sengaja tidak diuji (beserta alasannya).
- **Approach:** Strategi pengujian yang digunakan (manual/otomatis, jenis testing).
- **Item Pass/Fail Criteria:** Kriteria kelulusan item yang diuji.
- **Suspension & Resumption Criteria:** Kriteria kapan pengujian harus dihentikan sementara dan kapan bisa dilanjutkan.
- **Test Deliverables:** Dokumen apa saja yang akan diserahkan setelah selesai.
- **Testing Tasks:** Daftar tugas pengujian yang harus dilakukan.
- **Environmental Needs:** Kebutuhan infrastruktur (perangkat keras, perangkat lunak, jaringan).
- **Responsibilities:** Pembagian tugas dan tanggung jawab tim.
- **Staffing & Training Needs:** Kebutuhan personel dan pelatihan khusus jika ada.
- **Schedule:** Jadwal berkala pelaksanaan uji.
- **Risks and Contingencies:** Risiko yang mungkin terjadi dan rencana cadangannya.
- **Approvals:** Tanda tangan persetujuan dari pihak terkait (stakeholders).

### B. Test Design Specification (Spesifikasi Desain Uji)

Merinci refinasi dari pendekatan pengujian yang ada di Test Plan ke dalam fitur yang lebih spesifik.

- **Test Design Identifier:** ID unik dokumen.
- **Features to be Tested:** Detail fitur yang akan dicakup oleh desain ini.
- **Approach Refinement:** Penajaman metode uji khusus untuk fitur tersebut.
- **Test Case Identification:** Daftar ID test case yang terikat dengan desain ini.
- **Feature Pass/Fail Criteria:** Kriteria lulus/gagal untuk fitur spesifik tersebut.

### C. Test Case Specification (Spesifikasi Kasus Uji)

Dokumen yang mendefinisikan sekumpulan input, kondisi eksekusi, dan hasil yang diharapkan.

- **Test Case Identifier:** ID unik untuk setiap kasus uji.
- **Test Items:** Item spesifik yang diuji oleh case ini.
- **Input Specifications:** Data masukan yang diperlukan (berupa file, nilai, atau aksi).
- **Output Specifications:** Hasil atau perilaku sistem yang diharapkan (expected result).
- **Environmental Needs:** Pengaturan lingkungan khusus untuk menjalankan test case ini.
- **Special Procedural Requirements:** Prosedur khusus (jika ada) saat mengeksekusi.
- **Intercase Dependencies:** Ketergantungan antar test case (misal: Case B hanya bisa jalan jika Case A sukses).

### D. Test Procedure Specification (Spesifikasi Prosedur Uji)

Langkah-langkah detail atau instruksi kerja (seperti test script) untuk menjalankan kasus uji.

- **Test Procedure Identifier:** ID unik prosedur.
- **Purpose:** Tujuan dari prosedur ini dijalankan.
- **Special Requirements:** Prasyarat khusus sebelum memulai (misal: kondisi database tertentu).
- **Procedure Steps:** Langkah demi langkah konkret (Log masuk $\rightarrow$ Klik tombol $\rightarrow$ Verifikasi hasil).

## 2. Fase Eksekusi Pengujian (Test Execution)

Fase saat pengujian benar-benar dijalankan dan hasilnya dicatat secara berkala.

### A. Test Item Transmittal Report (Laporan Serah Terima Item)

Digunakan jika tim pengembang (developer) menyerahkan produk secara formal kepada tim penguji (tester).

- **Transmittal Identifier:** ID unik serah terima.
- **Items Transmitted:** Daftar modul/aplikasi versi berapa yang diserahkan.
- **Location:** Lokasi fisik atau path penyimpanan file/aplikasi tersebut.
- **Status:** Status saat ini (apakah ada bug krusial yang sudah diketahui sebelumnya).
- **Approvals:** Tanda tangan serah terima kedua belah pihak.

### B. Test Log (Catatan Pengujian)

Catatan kronologis yang merekam detail pelaksanaan pengujian secara real-time.

- **Test Log Identifier:** ID unik log.
- **Description:** Informasi kapan pengujian dilakukan, oleh siapa, dan lingkungan yang dipakai.
- **Execution Description:** Catatan aktivitas pengujian (misal: Jam 09.00 menjalankan Prosedur X).
- **Result:** Hasil aktual (Actual Result), apakah Pass (Lulus) atau Fail (Gagal).
- **Environmental Information:** Kondisi lingkungan saat itu (misal: server sempat down 10 menit).
- **Anomalies:** Kejadian tidak biasa yang ditemukan saat eksekusi.

### C. Test Incident Report (Laporan Insiden / Bug Report)

Dokumen untuk mencatat setiap anomali atau kegagalan yang terjadi selama pengujian yang membutuhkan investigasi lebih lanjut.

- **Incident Report Identifier:** ID unik laporan bug.
- **Summary:** Ringkasan singkat mengenai bug yang ditemukan.
- **Incident Description:** Detail lengkap insiden (waktu, langkah memicu bug/steps to reproduce, hasil aktual vs diharapkan).
- **Impact:** Tingkat keparahan (severity) dan prioritas perbaikan bug terhadap sistem.

## 3. Fase Penyelesaian Pengujian (Test Completion)

Fase evaluasi untuk merangkum seluruh aktivitas pengujian yang telah selesai dilakukan.

### A. Test Summary Report (Laporan Ringkasan Pengujian)

Dokumen final yang merangkum hasil seluruh aktivitas pengujian dan memberikan penilaian kualitas produk.

- **Summary Report Identifier:** ID unik laporan akhir.
- **Summary:** Evaluasi total terhadap apa yang diuji dan berapa lama prosesnya.
- **Variances:** Catatan jika ada perbedaan pelaksanaan dari rencana awal (Test Plan).
- **Comprehensiveness Assessment:** Penilaian seberapa menyeluruh pengujian telah dilakukan (apakah cakupan uji sudah terpenuhi).
- **Summary of Results:** Rangkuman hasil (Berapa banyak test case yang lulus, gagal, dan jumlah bug yang masih terbuka/open).
- **Evaluation:** Penilaian akhir tim QA mengenai kualitas sistem (apakah layak naik cetak/production atau tidak).
- **Summary of Activities:** Rincian total sumber daya, biaya, dan waktu yang dihabiskan.
- **Approvals:** Persetujuan akhir dari Manajer QA, Manajer Proyek, atau Klien untuk menutup fase testing.
