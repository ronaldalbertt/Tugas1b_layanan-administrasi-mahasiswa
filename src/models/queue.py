from collections import deque


class Queue:
    """Struktur data Queue dengan prinsip FIFO (First In First Out)."""

    def __init__(self):
        self.data = deque()

    def enqueue(self, data):
        """Menambahkan data ke bagian belakang antrean."""
        self.data.append(data)

    def dequeue(self):
        """Mengambil data paling depan. None jika antrean kosong."""
        if self.is_empty():
            return None
        return self.data.popleft()

    def peek(self):
        """Melihat data paling depan tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self.data[0]

    def is_empty(self):
        """Mengembalikan True jika antrean kosong."""
        return len(self.data) == 0

    def display(self):
        """Mengembalikan isi antrean dari depan ke belakang."""
        return list(self.data)

    def __len__(self):
        return len(self.data)
