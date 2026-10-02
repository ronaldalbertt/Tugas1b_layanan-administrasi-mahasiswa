import unittest

from src.models.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push("Aktivitas 1")
        stack.push("Aktivitas 2")
        self.assertEqual(stack.display(), ["Aktivitas 1", "Aktivitas 2"])

    def test_pop(self):
        stack = Stack()
        stack.push("Aktivitas 1")
        stack.push("Aktivitas 2")
        self.assertEqual(stack.pop(), "Aktivitas 2")
        self.assertEqual(stack.display(), ["Aktivitas 1"])

    def test_peek(self):
        stack = Stack()
        stack.push("Aktivitas 1")
        stack.push("Aktivitas 2")
        self.assertEqual(stack.peek(), "Aktivitas 2")
        self.assertEqual(stack.display(), ["Aktivitas 1", "Aktivitas 2"])

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push("Aktivitas 1")
        self.assertFalse(stack.is_empty())

    def test_pop_empty(self):
        stack = Stack()
        self.assertIsNone(stack.pop())


if __name__ == "__main__":
    unittest.main()
