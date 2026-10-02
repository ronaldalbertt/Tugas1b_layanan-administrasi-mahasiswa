class Stack:
    """Struktur data Stack dengan prinsip LIFO (Last In First Out)."""

    def __init__(self):
        self.data = []

    def push(self, data):
        """Menambahkan data ke posisi paling atas stack."""
        self.data.append(data)

    def pop(self):
        """Mengambil data paling atas. None jika stack kosong."""
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        """Melihat data paling atas tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        """Mengembalikan True jika stack kosong."""
        return len(self.data) == 0

    def display(self):
        """Mengembalikan isi stack dari bawah ke atas."""
        return list(self.data)

    def __len__(self):
        return len(self.data)
