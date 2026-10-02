from src.services.layanan_service import LayananAdministrasi

data_mahasiswa = [
    "Andi Pratama",
    "Budi Santoso",
    "Citra Lestari",
    "Deni Kurniawan",
    "Eko Saputra",
]


def tampilkan(kondisi):
    if kondisi:
        print("[" + " -> ".join(kondisi) + "]")
    else:
        print("[Antrean kosong]")


def main():
    layanan = LayananAdministrasi()

    print("=" * 65)
    print("SIMULASI ANTREAN LAYANAN MAHASISWA")
    print("=" * 65)

    langkah = 1
    for nama in data_mahasiswa:
        layanan.tambah_mahasiswa(nama)
        print(f"\nLangkah {langkah}")
        print("Operasi        : Enqueue / Penambahan data")
        print(f"Data diproses  : {nama}")
        print("Kondisi setelah:", end=" ")
        tampilkan(layanan.lihat_antrean())
        langkah += 1

    print(f"\nLangkah {langkah}")
    print("Operasi        : Peek / Melihat data terdepan")
    print(f"Data diproses  : {layanan.mahasiswa_terdepan()}")
    print("Kondisi setelah:", end=" ")
    tampilkan(layanan.lihat_antrean())
    langkah += 1

    print(f"\nLangkah {langkah}")
    dilayani = layanan.layani_mahasiswa()
    print("Operasi        : Dequeue / Pengambilan data")
    print(f"Data diproses  : {dilayani}")
    print("Kondisi setelah:", end=" ")
    tampilkan(layanan.lihat_antrean())
    langkah += 1

    print(f"\nLangkah {langkah}")
    print("Operasi        : IsEmpty / Memeriksa kondisi kosong")
    print(f"Data diproses  : Tidak ada")
    print(f"Kondisi setelah: {layanan.antrean_kosong()}")

    print("\n" + "=" * 65)
    print("HASIL AKHIR ANTREAN")
    print("=" * 65)
    tampilkan(layanan.lihat_antrean())


if __name__ == "__main__":
    main()
