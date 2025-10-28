import random
import unittest

from homework_5.avl import AVLTree


class TestAVLTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = AVLTree[int]()

    def test_insert_increases_height(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.height, 1)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertTrue(self.tree.height <= 2)

    def test_search_found(self):
        values = [10, 20, 5, 4, 15]
        for value in values:
            self.tree.insert(value)
        for value in values:
            self.assertTrue(self.tree.search(value))

    def test_search_not_found(self):
        values = [10, 20, 5]
        for value in values:
            self.tree.insert(value)
        self.assertFalse(self.tree.search(100))

    def test_delete_leaf(self):
        for value in [10, 20, 5]:
            self.tree.insert(value)
        self.tree.delete(5)
        self.assertFalse(self.tree.search(5))

    def test_delete_root(self):
        for value in [20, 10, 30, 25, 40]:
            self.tree.insert(value)
        self.tree.delete(20)
        self.assertFalse(self.tree.search(20))
        self.assertTrue(self.tree.height >= 0)

    def test_balanced_after_random_operations(self):
        values = random.sample(range(1000), 50)
        for value in values:
            self.tree.insert(value)

        random.shuffle(values)
        for value in values[:10]:
            self.tree.delete(value)

        def is_balanced(node):
            if node is None:
                return True, 0
            left_balanced, left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            return balanced, height

        balanced, _ = is_balanced(self.tree._root)
        self.assertTrue(balanced)


if __name__ == "__main__":
    unittest.main()

