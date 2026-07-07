# 🎓 Sistem Prioritas Penerima Beasiswa - Analisis Algoritma (Topik 7)
### Program Studi Ilmu Komputer - Universitas Putra Bangsa

Project Kelompok ini dibuat untuk memenuhi tugas besar mata kuliah **Analisis Algoritma (Durasi 2 Minggu)** di bawah bimbingan Dosen Pengampu **Bapak Awaludin Abid, S.Kom., M.Kom.**

---

## 👥 Identitas Kelompok & Pembagian Tugas
Berikut adalah susunan anggota kelompok 7 beserta kontribusi nyata dalam pengembangan sistem:

1. **Andri Dwi Yuliyanto (NIM: 250202976)**
2. **Ahmad Rohisun  (NIM: 250202984)**
3. **Latifah Risti Anggraeni (NIM: 250202945)**
4. **Miftakhul Lisna Esa Baehaqi (NIM: 250202951)**


---

## 🚀 Deskripsi Project
Aplikasi ini merupakan sistem manajemen dan seleksi prioritas penerima beasiswa berbasis *Console interaktif*. Sistem menggunakan metode pembobotan (*Weighted Scoring*) berdasarkan 4 kriteria utama: IPK (40%), Faktor Penghasilan Orang Tua (30%), Jumlah Tanggungan (20%), dan Jumlah Prestasi (10%).

Aplikasi diimplementasikan menggunakan **Arsitektur Modular** untuk memisahkan setiap kompartemen logika guna mempermudah kolaborasi tim (*version control friendly*).

### Komparasi Komputasi & Struktur Data Inti:
* **Algoritma Pengurutan:** *Selection Sort* ($O(n^2)$) vs *Merge Sort* ($O(n \log n)$) [Ditulis Manual]
* **Struktur Data:** *Array/List* (Penyimpanan Utama) dan *Max-Heap / Priority Queue* (Proses Seleksi Kuota) [Ditulis Manual]

---

## 📂 Struktur Repositori Modular
Berikut adalah berkas-berkas program yang menyusun sistem ini:
1. **`main.py`**: Berkas utama (*entry point*) aplikasi yang mengatur jalannya program dan menyediakan antarmuka menu interaktif (CRUD & Seleksi).
2. **`models.py`**: Menangani representasi data mahasiswa serta rumus matematika perhitungan skor prioritas beasiswa.
3. **`algoritma.py`**: Implementasi murni (*pure Python*) dari algoritma *Selection Sort* dan *Merge Sort*.
4. **`struktur_data.py`**: Implementasi murni kelas struktur data *Max-Heap Priority Queue* untuk ekstraksi kuota berprioritas tinggi.
5. **`pengujian.py`**: Menyediakan generator data sintetis otomatis serta modul eksperimen pencatatan waktu eksekusi sebanyak 5x pengulangan.

---

## ✨ Fitur Aplikasi
1. **Manajemen Data Mahasiswa (CRUD):** Tambah (Create), Lihat Semua Data (Read), Ubah Data (Update), dan Hapus Data (Delete) dengan format NIM otomatis `2502029xx`.
2. **Proses Seleksi Beasiswa (Max-Heap):** Menyaring sejumlah $N$ mahasiswa prioritas tertinggi sesuai kuota menggunakan operasi `extract_max()` pada struktur data Heap secara dinamis, transparan, dan cepat.
3. **Eksperimen Analisis Komputasi:** Menguji kecepatan running-time kedua algoritma sorting secara massal pada skala **100, 500, 1.000, hingga 5.000 data** dengan 5 kali pengulangan otomatis untuk mencari nilai rata-rata eksekusi (*millisecond*).

---

## 💻 Cara Menjalankan Program

### Prasyarat
* Pastikan perangkat Anda sudah terinstal **Python 3.x**.

### Langkah Eksekusi
1. Unduh atau *clone* seluruh isi folder repositori ini.
2. Buka terminal, command prompt, atau terminal IDE (seperti VS Code) di dalam direktori folder tempat berkas-berkas kode berada.
3. Jalankan berkas utama dengan perintah berikut:
   ```bash
   python main.py
