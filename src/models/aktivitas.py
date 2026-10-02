from dataclasses import dataclass


@dataclass
class Aktivitas:
    """Merepresentasikan satu riwayat aktivitas petugas untuk fitur Undo."""

    tanggal_jam: str
    jenis: str
    deskripsi: str

    def __str__(self):
        return f"{self.tanggal_jam} | {self.jenis} | {self.deskripsi}"
