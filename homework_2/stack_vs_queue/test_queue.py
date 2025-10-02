import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_and_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.size(), 2)

        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.size(), 3)

    def test_peek_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_queue_order(self):
        self.queue.enqueue("first")
        self.queue.enqueue("second")
        self.queue.enqueue("third")

        self.assertEqual(self.queue.dequeue(), "first")
        self.assertEqual(self.queue.dequeue(), "second")
        self.assertEqual(self.queue.dequeue(), "third")

    def test_multiple_operations(self):
        for i in range(10):
            self.queue.enqueue(i)

        self.assertEqual(self.queue.size(), 10)
        self.assertEqual(self.queue.peek(), 0)

        for i in range(10):
            self.assertEqual(self.queue.dequeue(), i)

        self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()

