# Tugas Mandiri 1b — Penerapan Struktur Data Linear

Project ini dibuat berdasarkan studi kasus pada Tugas Mandiri 1b mata kuliah Struktur Data.
Fokus project adalah dua kebutuhan sistem layanan administrasi mahasiswa:

1. **Antrean layanan mahasiswa** menggunakan **Queue** dengan prinsip **FIFO (First In First Out)**.
2. **Fitur Undo** menggunakan **Stack** dengan prinsip **LIFO (Last In First Out)**.

## Struktur Project

```text
tugas1b-struktur-data-linear/
├── main.py
├── README.md
├── .gitignore
├── src/
│   ├── models/
│   │   ├── queue.py
│   │   ├── stack.py
│   │   └── aktivitas.py
│   └── services/
│       └── layanan_service.py
├── simulation/
│   ├── simulasi_antrean.py
│   └── simulasi_undo.py
└── tests/
    ├── test_queue.py
    └── test_stack.py
```

## Operasi Utama

### Queue
- `enqueue()` — menambah mahasiswa ke belakang antrean.
- `dequeue()` — mengambil/melayani mahasiswa paling depan.
- `peek()` — melihat mahasiswa paling depan tanpa menghapusnya.
- `is_empty()` — memeriksa apakah antrean kosong.

### Stack
- `push()` — menyimpan aktivitas baru.
- `pop()` — mengambil/membatalkan aktivitas terakhir.
- `peek()` — melihat aktivitas paling atas.
- `is_empty()` — memeriksa apakah riwayat Undo kosong.

## Menjalankan Program Utama

```bash
python main.py
```

## Menjalankan Simulasi

Antrean:

```bash
python -m simulation.simulasi_antrean
```

Undo:

```bash
python -m simulation.simulasi_undo
```

## Menjalankan Unit Testing

```bash
python -m unittest discover -v
```

## Pemetaan ke Lembar Aktivitas

- Nomor 1: karakteristik permasalahan dan operasi.
- Nomor 2: program Python dan repository GitHub.
- Nomor 3–4: Queue untuk antrean dan Stack untuk Undo, beserta alasan.
- Nomor 5 dan 7: data serta simulasi antrean.
- Nomor 6 dan 9: data serta simulasi aktivitas Undo.
- Nomor 8 dan 10: screenshot kode simulasi.
- Nomor 11 dan 13: kesimpulan kondisi sebelum/sesudah simulasi.
- Nomor 12 dan 14: Unit Testing.
- Nomor 15: analisis kompleksitas waktu.
