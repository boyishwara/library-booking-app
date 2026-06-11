# MASTER TEST PLAN PENGUJIAN PERANGKAT LUNAK SISTEM EVENT ORGANIZER

**Disusun Oleh:**
* Ar Ramarega Dheriva (115060807111089)
* Briandana Riznov (115060807111025)
* Fahmi Rizqon Faizin (115060807111040)
* Ryan Ramadhan (115060800111042)

**PROGRAM STUDI TEKNIK INFORMATIKA**
**PROGRAM TEKNOLOGI INFORMASI DAN ILMU KOMPUTER**
**UNIVERSITAS BRAWIJAYA**
**MALANG**
**2015**

---

## SEO TEST DESIGN SPECIFICATION
**SEO Software Project – Phase 1**

### Version History
| Version | Date | Authors | Status |
| :--- | :--- | :--- | :--- |
| 1.00 | 13-01-2015 | Briandana Riznov | |

### Test Design Document Contents
* Test Plan Identifier
* Introduction
* Test Item(s)
* Features to be Tested
* Features Not to be Tested
* Approach/Strategy
* Item Pass/Fail Criteria
* Suspension Criteria and Resumption Requirements
* Test Deliverables
* Remaining Test Tasks
* Test Environments
* Responsibilities
* Staffing and Training Needs
* Schedule
* Risks and Contingencies

---

### A. Test Plan Identifier
Identifier untuk Test Plan Sistem Event Organizer ini adalah SEOTP-001, sedangkan untuk Test Design adalah SEOTD-001. Dengan catatan struktur dokumen ini secara utama berdasarkan pada standar IEEEE 829-1998 untuk dokumentasi pengujian perangkat lunak.

### B. Introduction
Untuk dapat menghasilkan proses yang efisien, efektif, dan hasil yang optimal pada suatu event, kami merasa dibutuhkan suatu sistem yang terintegrasi dan dapat berkembang untuk mengorganisir kegiatan-kegiatan pada event tersebut. Pengguna sistem ini adalah panitia-panitia SEO yang dibagi menjadi empat departemen atau modul, yaitu: HRD, Keuangan, Event, dan Marketing. Pada Test Plan ini akan diuji tiga fitur dari modul HRD, yakni: Tambah pegawai, Hapus pegawai, dan Edit pegawai.

### C. Test Item(s)
Batasan dari pengujian ini menyangkup Aplikasi Web SEO v.1.0 khususnya pada modul HRD.

### D. Features to be Tested
Tahapan-tahapan pada pengujian ini terfokus pada fitur-fitur sebagai berikut:
a. Fitur tambah pegawai
b. Fitur edit pegawai
c. Fitur hapus pegawai

### E. Features Not to be Tested
Fitur-fitur yang tidak diuji adalah semua fitur yang terdapat pada modul Event, Keuangan, dan Marketing.

### F. Approach/Strategy
Setiap Test Case akan diprioritaskan dengan tingkatan High, Medium, atau Low, dimana ketiga fitur yang diuji akan diprioritaskan sebagai High. Pengujian akan dilakukan secara manual untuk tiap-tiap fitur.

*   **Data and Database Integrity Testing**
    *   **Test Objective:** Query dapat menghasilkan informasi sesuai yang dibutuhkan.
    *   **Technique:** Melakukan query select pada database.
    *   **Completion Criteria:** Database dapat query dengan baik.
    *   **Special Considerations:** -
*   **Function Testing**
    *   **Test Objective:** Hasil input data dapat masuk ke database dengan benar dan Tampilan output sesuai dengan database.
    *   **Technique:** Mencocokkan hasil input dan output pada aplikasi dengan hasil input dan output di database.
    *   **Completion Criteria:** Hasil input dan output pada aplikasi sesuai dengan database.
    *   **Special Considerations:** -
*   **Business Cycle Testing**
    *   **Test Objective:** Sistem dapat merekam semua kegiatan yang terjadi dalam jangka waktu tertentu.
    *   **Technique:** Menguji log dan data-data sistem.
    *   **Completion Criteria:** Sistem dapat menampilkan data disertai keterangan tanggal.
    *   **Special Considerations:** -
*   **User Interface Testing**
    *   **Test Objective:** Tampilan sistem bekerja dengan baik.
    *   **Technique:** Menguji tampilan field dan tombol pada form, tampilan hyperlink, dan penempatan komponen-komponen di tiap halaman.
    *   **Completion Criteria:** Tampilan aplikasi terletak secara baik dan user friendly.
    *   **Special Considerations:** Testing dilakukan pada platform yang berada dalam kemampuan sistem.
*   **Performance Profiling**
    *   **Test Objective:** Proses transaksi data bekerja dengan cepat.
    *   **Technique:** Melakukan timing untuk setiap proses yang menggunakan database.
    *   **Completion Criteria:** Tiap pemrosesan data pada aplikasi membutuhkan waktu kurang dari 5 detik.
    *   **Special Considerations:** -
*   **Installation Testing**
    *   **Test Objective:** Menguji keberhasilan instalasi sistem.
    *   **Technique:** Melakukan pemindahan source code dan database sistem ke komputer lain.
    *   **Completion Criteria:** Sistem dapat diinstalasikan pada komputer lain.
    *   **Special Considerations:** Komputer lain harus memenuhi kebutuhan sistem.
*   **Security and Access Control Testing**
    *   **Test Objective:** Aksesibilitas semua fitur pada sistem sesuai dengan aturan yang telah ditentukan.
    *   **Technique:** Mencoba melakukan suatu proses tanpa memiliki hak akses.
    *   **Completion Criteria:** Proses tidak dapat dilakukan.
    *   **Special Considerations:** Pengujian menggunakan user selain Super-Admin.

### G. Item Pass/Fail Criteria
Kriteria lolos untuk tiap fase harus terpenuhi sebelum pengujian beranjak menuju fase selanjutnya, dimana persetujuan akan dilakukan oleh Project Manager SEO. Project Manager SEO akan menentukan semua keputusan pengujian menyangkup tingkat keparahan semua defect yang terdeteksi pada sistem ini.

### H. Suspension Criteria and Resumption Requirements
Pengujian akan dihentikan jika terjadi masalah pada localhost, dan akan dilanjutkan kembali secepatnya setelah masalah localhost telah diatasi.

### I. Test Deliverables
Dokumen-dokumen berikut akan dihasilkan setelah aktivitas pengujian dilakukan:
a. Master Test Plan
b. Test Design
c. Test Procedure
d. Test Case
e. Test Summary

### J. Remaining Test Tasks
Setelah lengkapnya test delivarebles dan berhasilnya penginstalan sistem ini pada lingkungan produksi, maka semua kegiatan pada Master Plan ini dapat dikatakan telah lengkap, dengan pengecualian jika terdapat post-implementation test plan pada versi selanjutnya yang akan terus dilakukan hingga aplikasi ini tidak digunakan lagi.

### K. Test Environments
Dikarenakan kebutuhan spesifikasi sistem yang ringan, maka lingkungan pengujian ini dilakukan dengan spesifikasi Medium-end Laptop Intel Core i3 2350M CPU @ 2.30 GHz, 2GB RAM, 500 GB HDD Space dengan koneksi localhost (XAMPP Control Panel v3.1.0 beta 6), Google Chrome v39.0.2171.95 m, dan Notepad++ v.6.6.8.

### L. Responsibilities
Penguji-penguji dibawah ini bertanggung jawab atas:
a. Briandana Riznov (115060807111025) – Test Procedure
b. Ryan Ramadhan (115060800111042) – Test Design dan Summary
c. Ar Ramarega Dheriva (115060807111089) – Test Case
d. Fahmi Rizqon (115060807111040) – Test Case

### M. Staffing and Training Needs
Penguji-penguji pada pengujian ini dapat dipastikan memenuhi standar keterampilan sebagai berikut:
a. Pengembangan dan pengujian secara umum
b. Metode life-cycle pengembangan SEO
c. Penggunaan alat-alat pengujian SEO

### N. Schedule
Master Test Plan ini diharapkan dapat rampung dalam waktu satu minggu dari awal pengerjaan dengan batas akhir Hari Kamis tanggal 15 Januari 2015 yakni hari presentasi Test Plan ini.

### O. Risks and Contingencies
Hal-hal berikut merupakan resiko yang mungkin terjadi pada pengujian ini dan dapat menyebabkan kemunduran laju proyek:
a. Masalah pada localhost yang menjadi penyedia utama pengujian sistem ini.
b. Ketidaktersediaan penguji.
c. Ditemukannya defect yang terlalu banyak yang menyebabkan pengujian test case terhambat secara fungsional.
d. Ketidaktersediaan waktu pengujian test case.

---

## SEO TEST PROCEDURE SPECIFICATION
Dokumen ini terkait dengan test plan SEOTP-001.

### A. OUTLINE
Secara singkat, untuk prosedur atau langkah yang perlu dilakukan dalam melakukan tes disini memiliki struktur sebagai berikut:
a. Test procedure specification identifier
b. Purpose
c. Special requirements
d. Procedure steps

### B. TEST PROCEDURE SPECIFICATION IDENTIFIER
Identifier untuk dokumen ini adalah SEOTPR-001.

### C. PURPOSE
Untuk mendeskripsikan secara jelas langkah-langkah yang harus dilakukan untuk mengeksekusi set dari test case, atau yang lebih umum. Langkah-langkah yang digunakan untuk menganalisa sebuah software dengan tujaun untuk mengevaluasi fitur-fitur yang ada didalamnya.

### D. SPECIAL REQUIREMENT
* Membutuhkan sedikit pengetahuan tentang membaca dokumentasi, baik pada dokumen tes sebelumnya maupun pada kode program.
* Skill dasar kode program.
* Memahami flow process program.

### E. PROCEDURE STEPS
*   **Tambah Pegawai Test Procedure**
    1. Masuk / login sebagai admin HRD.
    2. Halaman awal muncul adalah halaman pegamai, pilih tambah pegawai.
    3. Setelah muncul halaman baru, terdapat field input yang harus diisikan sebelum disimpan.
    4. Selesai diisikan pilih tombol save.
*   **Edit Pegawai Test Procedure**
    1. Pada halaman awal saat pertama kali masuk / login terdapat field berisikan data pegawai yang telah disimpan.
    2. Pada setiap pegawai terdapat dua tombol yang berisikan edit dan hapus.
    3. Pilih edit pada pegawai yang ingin diedit.
    4. Setelah itu akan muncul field input yang sesuai dengan isian pegawai yang telah disimpan.
    5. Selesai di edit pilih tombol save.
*   **Hapus Pegawai Test Procedure**
    1. Pada halaman awal saat pertama kali masuk / login terdapat field berisikan data pegawai yang telah disimpan.
    2. Pada setiap pegawai terdapat dua tombol yang berisikan edit dan hapus.
    3. Pilih hapus pada pegawai yang ingin dihapus.
    4. Setelah itu akan muncul field input yang sesuai dengan isian pegawai yang telah disimpan.
    5. Selesai di edit pilih tombol save.

---

## SEO TEST CASE
Identifier dokumen ini adalah SEOTC-001.

### A. Performance
*   **Tool Pengujian:** Web Server Stress Tool
*   **Tujuan:** Menguji Pengaturan Jumlah Dan Waktu User Menggunakan Aplikasi Ini
*   **Objeck Yang Diuji:** Aplikasi Sistem Event Organizer

Adapun Tahapan yang digunakan yaitu: Waktu Klik, Rata – rata waktu klik, Waktu DNS, Waktu Koneksi, Waktu untuk byte pertama (T F B), Waktu Permintaan, User / Server Brandwidth, Pengiriman Permintaan, Penerimaan Permintaan, Membuka Permintaan.

**Kesimpulan:**
1. Dari hasil Result User didapatkan kecepatan average click time yaitu 296 milisekon. Dengan begitu berarti sistem dapat melayani request user dengan cukup cepat. Dengan waktu yang cukup cepat admin dapat menambahkan pegawai tanpa terjadi eror. Jadi dapat di simpulkan bahwa performa dari aplikasi ini cukup baik.
2. Dari Hasil Result URL didapatkan bahwa aplikasi jumlah request sebesar 5 kali menghasilkan response time sebesar 887 milisekon. Jadi dari data yang ditampilkan di atas menunjukkan bahwa performa dari aplikasi ini cukup baik untuk melayani request di bawah 1 detik.

### B. State transition diagram
**a. Tambah Pegawai Test Case**
| Status | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| Mulai | S(1) | S(2) | S(3) | S(3) |
| Masukan | KTTP | KTT | NSD | PBA |
| Keluaran | PFTP | PD | INYD | SP |
| Selesai | S(2) | S(3) | S(2) | S(1) |
**Kesimpulan:** Transisi Valid.

**b. Edit Pegawai Test Case**
| Status | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| Mulai | S(1) | S(2) | S(3) | S(3) |
| Masukan | KTEP | KET | NSD | PBA |
| Keluaran | PFEP | PD | INYD | SP |
| Selesai | S(2) | S(3) | S(2) | S(1) |
**Kesimpulan:** Transisi Valid.

**c. Hapus Pegawai Test Case**
| Status | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- |
| Mulai | S(1) | S(2) | S(3) |
| Masukan | KTDP | KDT | PBD |
| Keluaran | PFDP | PD | PGD |
| Selesai | S(2) | S(3) | S(1) |
**Kesimpulan:** Transisi Valid.

### C. Test Strategy Function Testing
Teknik pengujian sesuai dengan Test Case berdasarkan skenario pengujian. Tujuan desain Test Case adalah untuk mendapatkan hasil dari serangkaian pengujian yang memiliki kemungkinan tertinggi untuk menemukan kesalahan pada perangkat lunak.

| Skenario | Username | Password | Hasil |
| :--- | :--- | :--- | :--- |
| Edit Pegawai | hrd | 1234 | Dapat melakukan editing pegawai dengan ketentuan harus di isi dengan benar |
| Tambah Pegawai | hrd | 1234 | Dapat menambahkan Pegawai dengan inputan sesuai yang diminta aplikasi |
| Hapus Pegawai | hrd | 1234 | Dapat melakukan Penghapusan terhadapap Pegawai |

### D. Hasil Pengujian
* Tambah Pegawai (Valid)
* Hapus Pegawai (Valid)
* Edit Pegawai (Valid)

### E. Basis Path – White Box Testing

**a. Tambah Pegawai**
```php
class Pegawai extends CI_Controller {
    public function index() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $data['pegawai']=$this->Pegawai_model->get_all_pegawai();
        $this->load->view('pegawai/index',$data);
    }
    public function add_form() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $data['jk']=$this->Pegawai_model->get_jk();
        $data['jabatan']=$this->Pegawai_model->get_jabatan();
        $this->load->view('pegawai/add',$data);
    }
    public function add_pegawai() {
        $np=$this->input->post('nama_pegawai');
        $ijk=$this->input->post('id_jk');
        $ijb=$this->input->post('id_jabatan');
        $ap=$this->input->post('alamat_pegawai');
        $tp=$this->input->post('telp_pegawai');
        $g=$this->input->post('gaji');
        $this->Pegawai_model->insert($np,$ijk,$ijb,$ap,$tp,$g);
        redirect('pegawai/');
    }
}
```
*   **Jalur:**
    Jalur 1 : 1-2-4-5-6-7-8-9-10-11-12
    Jalur 2 : 1-2-3-1-2-4-5-6-7-9-10-11-12
    Jalur 3 : 1-2-4-5-6-7-8-6-7-9-10-11-12
*   **V(G)** = E – N + 2 = 13 -12 + 2 = 3

**b. Edit (Update) Pegawai**
```php
class Pegawai extends CI_Controller {
    public function index() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $data['pegawai']=$this->Pegawai_model->get_all_pegawai();
        $this->load->view('pegawai/index',$data);
    }
    public function add_form() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $data['jk']=$this->Pegawai_model->get_jk();
        $data['jabatan']=$this->Pegawai_model->get_jabatan();
        $this->load->view('pegawai/update',$data);
    }
    public function Update_pegawai() {
        $ip=$this->input->post('id_pegawai');
        $np=$this->input->post('nama_pegawai');
        $ijk=$this->input->post('id_jk');
        $ijb=$this->input->post('id_jabatan');
        $ap=$this->input->post('alamat_pegawai');
        $tp=$this->input->post('telp_pegawai');
        $g=$this->input->post('gaji');
        $this->Pegawai_model->update($ip,$np,$ijk,$ijb,$ap,$tp,$g);
        redirect('pegawai/');
    }
}
```
*   **Jalur:**
    Jalur 1 : 1-2-4-5-6-7-8-9-10-11-12
    Jalur 2 : 1-2-3-1-2-4-5-6-7-9-10-11-12
    Jalur 3 : 1-2-4-5-6-7-8-6-7-9-10-11-12
*   **V(G)** = E – N + 2 = 13 -12 + 2 = 3

**c. Hapus (Delete) Pegawai**
```php
class Pegawai extends CI_Controller {
    public function index() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $data['pegawai']=$this->Pegawai_model->get_all_pegawai();
        $this->load->view('pegawai/index',$data);
    }
    public function add_form() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $data['jk']=$this->Pegawai_model->get_jk();
        $data['jabatan']=$this->Pegawai_model->get_jabatan();
        $this->load->view('pegawai/delete',$data);
    }
    public function delete_pegawai() {
        if($this->Auth_model->check_session()== FALSE){
            redirect('auth/');
        }
        $id = $this->uri->segment(3);
        $this->Pegawai_model->delete($id);
        redirect('pegawai/');
    }
}
```
*   **Jalur:**
    Jalur 1 : 1-2-4-5-6-7-8-9-10-11-12
    Jalur 2 : 1-2-3-1-2-4-5-6-7-9-10-11-12
    Jalur 3 : 1-2-4-5-6-7-8-6-7-9-10-11-12
*   **V(G)** = E – N + 2 = 13 -12 + 2 = 3

### F. Decision Table testing
Digunakan untuk menguji logika dari system dan termasuk dalam black box testing, dimana terdapat kondisi dan aksi. Kondisi merupakan inputan yang meimiliki output yang benar, dan aksi adalah aturan yang menjadi test casenya.

**a. Tambah Pegawai**
| Kondisi | Rule Y | Rule N |
| :--- | :--- | :--- |
| Input Nama Pegawai | √ | √ |
| Input Jenis Kelamin | √ | √ |
| Input Jabatan | √ | √ |
| Input Alamat Pegawai | √ | √ |
| Input Telefon Pegawai | √ | √ |
| Input Gaji Pegawai | √ | √ |
| **Aksi: Proses Penambahan berhasil?** | **Ya** | **Tidak** |

**b. Edit Pegawai**
| Kondisi | Rule Y | Rule N |
| :--- | :--- | :--- |
| Edit Nama Pegawai | √ | √ |
| Edit Jenis Kelamin | √ | √ |
| Edit Jabatan | √ | √ |
| Edit Alamat Pegawai | √ | √ |
| Edit Telefon Pegawai | √ | √ |
| Edit Gaji Pegawai | √ | √ |
| **Aksi: Proses Pengeditan berhasil?** | **Ya** | **Tidak** |

**c. Hapus Pegawai**
| Kondisi | Rule Y | Rule N |
| :--- | :--- | :--- |
| Delete Pegawai | √ | x |
| **Aksi: Proses Delete berhasil?** | **Ya** | **x** |

---

## SEO TEST SUMMARY

### A. TEST SUMMARY REPORT IDENTIFIER
Identifier untuk dokumen ini adalah SEOTS-001. Dokumen ini terkait dengan dokumen test plan, test design, test procedure, dan test case.

### B. SUMMARY
Sistem Event Organizer (SEO) merupakan sistem informasi yang bertujuan untuk mengorganisir kegiatan-kegiatan pada suatu event. SEO terdiri dari empat modul, yaitu: HRD, Event, Marketing, dan Keuangan. Pengujian yang dilakukan pada sistem ini ditekankan pada fitur tambah, edit, dan hapus pegawai pada modul HRD dengan modul Master Test Plan: Test Design, Test Procedure, Test Case, Test Summary.

### C. VARIANS
Laporan tiap varian dari test specification adalah sebagai berikut:
- **Test Design:** Pada pengujian ini dijelaskan tentang pengenalan dan deskripsi pengujian sistem SEO beserta fitur-fiturnya dengan hasil prioritas High untuk semua fitur.
- **Test Procedure:** Pada pengujian ini dijelaskan langkah-langkah yang diambil pada proses pengujian semua fitur dan mengevaluasinya.
- **Test Case:** Pada pengujian ini dijelaskan mengenai performance, hasil pengujian, transition diagram, test strategy, basis path, dan decision table.
- **Test Summary:** Merupakan dokumen ini yang berisi tentang kesimpulan dari semua pengujian yang telah dilakukan.

### D. COMPREHENSIVE ASSESMENT
Kelengkapan pengujian pada tiap-tiap fitur adalah sebagai berikut:

| Fitur | Approach | Status |
| :--- | :--- | :--- |
| Tambah pegawai | Performance, State trasition diagram, Strategy function testing, Basis path testing, dan Decision table testing. | Lengkap |
| Edit pegawai | Performance, State trasition diagram, Strategy function testing, Basis path testing, dan Decision table testing. | Lengkap |
| Hapus pegawai | Performance, State trasition diagram, Strategy function testing, Basis path testing, dan Decision table testing. | Lengkap |

### E. SUMMARY OF RESULT
Semua fitur lolos pengujian tanpa ditemukan kesalahan pada tiap-tiap modul pengujian.

### F. EVALUATION
Tidak ditemukan kesalahan pada pengujian fitur tambah, edit, dan hapus pegawai sistem SEO dengan modul-modul pengujian yang digunakan.

### G. SUMMARY OF ACTIVITIES
| Tests | Begin: 10/01/2015 | Estimated Day(s) | Actual Day(s) |
| :--- | :--- | :--- | :--- |
| Test Design | | 2 | 1 |
| Test Procedure | | 2 | 1 |
| Test Case | | 7 | 1 |
| Test Summary | | 1 | 1 |
| Revision | | 1 | 1 |
| **Test End: 15/01/2015** | | **13** | **5** |

### H. Approvals
Persetujuan pada test plan ini sepenuhnya kewenangan Project Manager SEO Briandana Riznov.