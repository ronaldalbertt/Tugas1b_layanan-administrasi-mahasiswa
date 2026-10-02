from datetime import datetime

from src.models.aktivitas import Aktivitas
from src.models.queue import Queue
from src.models.stack import Stack


class LayananAdministrasi:
    """Service yang menghubungkan kebutuhan sistem dengan Queue dan Stack."""

    def __init__(self):
        self.antrean = Queue()
        self.riwayat_undo = Stack()

    # -------------------- ANTREAN --------------------
    def tambah_mahasiswa(self, nama):
        self.antrean.enqueue(nama)

    def layani_mahasiswa(self):
        return self.antrean.dequeue()

    def mahasiswa_terdepan(self):
        return self.antrean.peek()

    def antrean_kosong(self):
        return self.antrean.is_empty()

    def lihat_antrean(self):
        return self.antrean.display()

    # -------------------- UNDO --------------------
    def simpan_aktivitas(self, jenis, deskripsi, tanggal_jam=None):
        if tanggal_jam is None:
            tanggal_jam = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        aktivitas = Aktivitas(tanggal_jam, jenis, deskripsi)
        self.riwayat_undo.push(aktivitas)
        return aktivitas

    def undo_terakhir(self):
        return self.riwayat_undo.pop()

    def aktivitas_terakhir(self):
        return self.riwayat_undo.peek()

    def undo_kosong(self):
        return self.riwayat_undo.is_empty()

    def lihat_riwayat_undo(self):
        return self.riwayat_undo.display()
