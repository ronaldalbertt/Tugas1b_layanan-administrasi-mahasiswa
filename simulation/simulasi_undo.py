from src.services.layanan_service import LayananAdministrasi


aktivitas = [
    ("01-10-2026 08:00:00", "Tambah Data", "Menambahkan mahasiswa Andi Pratama"),
    ("01-10-2026 08:05:00", "Ubah Data", "Mengubah data mahasiswa Budi Santoso"),
    ("01-10-2026 08:10:00", "Ubah Data", "Mengubah data mahasiswa Citra Lestari"),
    ("01-10-2026 08:15:00", "Hapus Data", "Menghapus data mahasiswa Deni Kurniawan"),
    ("01-10-2026 08:20:00", "Tambah Data", "Menambahkan mahasiswa Eko Saputra"),
]


def tampilkan(stack_data):
    if not stack_data:
        print("[Riwayat Undo kosong]")
        return
    print("[Bawah]" )
    for nomor, item in enumerate(stack_data, start=1):
        penanda = " <- TOP" if nomor == len(stack_data) else ""
        print(f"{nomor}. {item}{penanda}")


def main():
    layanan = LayananAdministrasi()

    print("=" * 75)
    print("SIMULASI FITUR UNDO AKTIVITAS PETUGAS")
    print("=" * 75)

    langkah = 1
    for tanggal_jam, jenis, deskripsi in aktivitas:
        item = layanan.simpan_aktivitas(jenis, deskripsi, tanggal_jam)
        print(f"\nLangkah {langkah}")
        print("Operasi        : Push / Menyimpan aktivitas")
        print(f"Data diproses  : {item}")
        print("Kondisi setelah:")
        tampilkan(layanan.lihat_riwayat_undo())
        langkah += 1

    print(f"\nLangkah {langkah}")
    print("Operasi        : Peek / Melihat aktivitas teratas")
    print(f"Data diproses  : {layanan.aktivitas_terakhir()}")
    print("Kondisi setelah:")
    tampilkan(layanan.lihat_riwayat_undo())
    langkah += 1

    print(f"\nLangkah {langkah}")
    dibatalkan = layanan.undo_terakhir()
    print("Operasi        : Pop / Undo aktivitas terakhir")
    print(f"Data diproses  : {dibatalkan}")
    print("Kondisi setelah:")
    tampilkan(layanan.lihat_riwayat_undo())
    langkah += 1

    print(f"\nLangkah {langkah}")
    print("Operasi        : IsEmpty / Memeriksa kondisi kosong")
    print("Data diproses  : Tidak ada")
    print(f"Kondisi setelah: {layanan.undo_kosong()}")

    print("\n" + "=" * 75)
    print("HASIL AKHIR RIWAYAT UNDO")
    print("=" * 75)
    tampilkan(layanan.lihat_riwayat_undo())


if __name__ == "__main__":
    main()
