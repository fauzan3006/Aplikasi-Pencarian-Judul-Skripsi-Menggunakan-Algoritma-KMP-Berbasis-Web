# Aplikasi Pencarian Judul Skripsi Menggunakan Algoritma KMP Berbasis Web

## Deskripsi Proyek
Aplikasi Pencarian Judul Skripsi merupakan aplikasi berbasis web yang digunakan untuk membantu pengguna dalam melakukan pencarian data judul skripsi mahasiswa secara cepat dan akurat berdasarkan kata kunci tertentu. Aplikasi ini dikembangkan sebagai project mata kuliah **Desain dan Analisis Algoritma**.

Proses pencarian judul skripsi pada aplikasi ini menggunakan algoritma **Knuth–Morris–Pratt (KMP)**, yaitu algoritma pencocokan string yang efisien karena mampu menghindari perbandingan karakter yang berulang. Dengan penerapan algoritma KMP, aplikasi dapat menampilkan hasil pencarian secara konsisten dan tepat sesuai dengan kata kunci yang dimasukkan oleh pengguna.

---

## Tujuan Pengembangan
Tujuan dari pengembangan aplikasi ini adalah:
- Mengimplementasikan algoritma Knuth–Morris–Pratt (KMP) dalam kasus nyata pencarian judul skripsi
- Meningkatkan efisiensi pencocokan string pada proses pencarian data skripsi
- Membantu mahasiswa dan dosen dalam mencari referensi judul skripsi
- Menjadi media pembelajaran penerapan algoritma pencarian string
- Mengintegrasikan algoritma pencarian dengan aplikasi berbasis web

---

## Algoritma yang Digunakan
Algoritma yang digunakan pada aplikasi ini adalah **Knuth–Morris–Pratt (KMP)**.

Algoritma KMP bekerja dengan membangun tabel **Longest Proper Prefix which is also Suffix (LPS)** sebelum proses pencarian dimulai. Tabel ini digunakan untuk menentukan pergeseran pola ketika terjadi ketidaksesuaian karakter, sehingga indeks teks tidak perlu kembali ke awal.

Kompleksitas waktu algoritma KMP adalah **O(n + m)**, di mana:
- **n** adalah panjang teks (judul skripsi)
- **m** adalah panjang pola (kata kunci)

---

## Fitur Aplikasi
Fitur yang tersedia pada aplikasi ini antara lain:
- Pencarian judul skripsi berdasarkan kata kunci
- Pencocokan string menggunakan algoritma Knuth–Morris–Pratt (KMP)
- Penandaan (*highlight*) kata kunci pada judul skripsi yang ditemukan
- Menampilkan jumlah hasil pencarian
- Menampilkan data judul skripsi, nama penulis, dan NIM
- Antarmuka web sederhana dan mudah digunakan
- Pesan informasi ketika data tidak ditemukan

---

## Struktur File
Struktur direktori proyek adalah sebagai berikut:

Aplikasi-Pencarian-Judul-Skripsi-Menggunakan-Algoritma-KMP-Berbasis-Web/
├── app.py
├── dataset_skripsi_unismuh.csv
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── Dokumentasi/
│ ├── ui/
│ └── pengujian/
└── README.md

---

## Dataset
Dataset yang digunakan pada aplikasi ini disimpan dalam format **CSV** dan berisi:
- Judul skripsi
- Nama penulis
- Nomor Induk Mahasiswa (NIM)

Dataset digunakan sebagai sumber data utama dalam proses pencarian judul skripsi menggunakan algoritma KMP.

---

## Pengujian Sistem
Pengujian sistem dilakukan menggunakan metode **black box testing** dengan beberapa skenario, antara lain:
- Pengujian pencarian dengan kata kunci umum
- Pengujian pencarian dengan kata kunci spesifik atau frasa lengkap
- Pengujian pencarian data yang tidak terdapat dalam dataset

Hasil pengujian menunjukkan bahwa algoritma KMP mampu melakukan pencarian judul skripsi secara efisien dan akurat.

---

## Teknologi yang Digunakan
Teknologi yang digunakan dalam pengembangan aplikasi ini meliputi:
- Python
- Flask
- HTML
- CSS
- File CSV
- Algoritma Knuth–Morris–Pratt (KMP)
