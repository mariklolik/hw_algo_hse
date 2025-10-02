import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size(), 0)

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)

        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.size(), 3)

    def test_peek_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_stack_order(self):
        self.stack.push("first")
        self.stack.push("second")
        self.stack.push("third")

        self.assertEqual(self.stack.pop(), "third")
        self.assertEqual(self.stack.pop(), "second")
        self.assertEqual(self.stack.pop(), "first")

    def test_multiple_operations(self):
        for i in range(10):
            self.stack.push(i)

        self.assertEqual(self.stack.size(), 10)
        self.assertEqual(self.stack.peek(), 9)

        for i in range(10):
            self.assertEqual(self.stack.pop(), 9 - i)

        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()

