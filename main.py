from src.services.layanan_service import LayananAdministrasi


def tampilkan_antrean(layanan):
    data = layanan.lihat_antrean()
    if not data:
        print("Antrean kosong.")
    else:
        print("Antrean (depan -> belakang):")
        for nomor, nama in enumerate(data, start=1):
            print(f"{nomor}. {nama}")


def tampilkan_undo(layanan):
    data = layanan.lihat_riwayat_undo()
    if not data:
        print("Riwayat Undo kosong.")
    else:
        print("Riwayat Undo (bawah -> atas):")
        for nomor, aktivitas in enumerate(data, start=1):
            penanda = " <- TOP" if nomor == len(data) else ""
            print(f"{nomor}. {aktivitas}{penanda}")


def menu_antrean(layanan):
    while True:
        print("\n--- MENU ANTREAN ---")
        print("1. Tambah mahasiswa (enqueue)")
        print("2. Layani mahasiswa (dequeue)")
        print("3. Lihat mahasiswa terdepan (peek)")
        print("4. Cek antrean kosong (is_empty)")
        print("5. Tampilkan antrean")
        print("0. Kembali")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            nama = input("Nama mahasiswa: ").strip()
            if not nama:
                print("Nama tidak boleh kosong.")
            else:
                layanan.tambah_mahasiswa(nama)
                print(f"{nama} berhasil masuk antrean.")
                tampilkan_antrean(layanan)
        elif pilihan == "2":
            mahasiswa = layanan.layani_mahasiswa()
            if mahasiswa is None:
                print("Antrean kosong, tidak ada mahasiswa yang dilayani.")
            else:
                print(f"Mahasiswa yang dilayani: {mahasiswa}")
                tampilkan_antrean(layanan)
        elif pilihan == "3":
            mahasiswa = layanan.mahasiswa_terdepan()
            if mahasiswa is None:
                print("Antrean kosong.")
            else:
                print(f"Mahasiswa terdepan: {mahasiswa}")
                tampilkan_antrean(layanan)
        elif pilihan == "4":
            print("Apakah antrean kosong?", layanan.antrean_kosong())
        elif pilihan == "5":
            tampilkan_antrean(layanan)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")


def menu_undo(layanan):
    while True:
        print("\n--- MENU UNDO ---")
        print("1. Simpan aktivitas (push)")
        print("2. Batalkan aktivitas terakhir (pop)")
        print("3. Lihat aktivitas terakhir (peek)")
        print("4. Cek riwayat Undo kosong (is_empty)")
        print("5. Tampilkan riwayat Undo")
        print("0. Kembali")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            jenis = input("Jenis aktivitas: ").strip()
            deskripsi = input("Deskripsi aktivitas: ").strip()
            if not jenis or not deskripsi:
                print("Jenis dan deskripsi tidak boleh kosong.")
            else:
                aktivitas = layanan.simpan_aktivitas(jenis, deskripsi)
                print("Aktivitas berhasil disimpan:")
                print(aktivitas)
                tampilkan_undo(layanan)
        elif pilihan == "2":
            aktivitas = layanan.undo_terakhir()
            if aktivitas is None:
                print("Riwayat Undo kosong, tidak ada aktivitas yang dibatalkan.")
            else:
                print("Aktivitas yang dibatalkan:")
                print(aktivitas)
                tampilkan_undo(layanan)
        elif pilihan == "3":
            aktivitas = layanan.aktivitas_terakhir()
            if aktivitas is None:
                print("Riwayat Undo kosong.")
            else:
                print("Aktivitas terakhir:")
                print(aktivitas)
        elif pilihan == "4":
            print("Apakah riwayat Undo kosong?", layanan.undo_kosong())
        elif pilihan == "5":
            tampilkan_undo(layanan)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")


def main():
    layanan = LayananAdministrasi()

    while True:
        print("\n" + "=" * 50)
        print(" SISTEM LAYANAN ADMINISTRASI MAHASISWA")
        print("=" * 50)
        print("1. Menu Antrean")
        print("2. Menu Undo")
        print("3. Keluar")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            menu_antrean(layanan)
        elif pilihan == "2":
            menu_undo(layanan)
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
