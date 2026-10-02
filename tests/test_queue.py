import unittest

from src.models.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("Andi")
        queue.enqueue("Budi")
        self.assertEqual(queue.display(), ["Andi", "Budi"])

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("Andi")
        queue.enqueue("Budi")
        self.assertEqual(queue.dequeue(), "Andi")
        self.assertEqual(queue.display(), ["Budi"])

    def test_peek(self):
        queue = Queue()
        queue.enqueue("Citra")
        self.assertEqual(queue.peek(), "Citra")
        self.assertEqual(queue.display(), ["Citra"])

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue("Deni")
        self.assertFalse(queue.is_empty())

    def test_dequeue_empty(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())


if __name__ == "__main__":
    unittest.main()
