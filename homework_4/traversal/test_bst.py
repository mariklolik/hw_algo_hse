import unittest

from homework_4.traversal.bst import BinarySearchTree


class TestBinarySearchTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            self.tree.insert(value)

    def test_preorder(self):
        self.assertEqual(
            self.tree.preorder(),
            [8, 3, 1, 6, 4, 7, 10, 14, 13],
        )

    def test_inorder(self):
        self.assertEqual(
            self.tree.inorder(),
            [1, 3, 4, 6, 7, 8, 10, 13, 14],
        )

    def test_postorder(self):
        self.assertEqual(
            self.tree.postorder(),
            [1, 4, 7, 6, 3, 13, 14, 10, 8],
        )

    def test_reverse_preorder(self):
        self.assertEqual(
            self.tree.reverse_preorder(),
            [8, 10, 14, 13, 3, 6, 7, 4, 1],
        )

    def test_reverse_inorder(self):
        self.assertEqual(
            self.tree.reverse_inorder(),
            [14, 13, 10, 8, 7, 6, 4, 3, 1],
        )

    def test_reverse_postorder(self):
        self.assertEqual(
            self.tree.reverse_postorder(),
            [13, 14, 10, 7, 4, 6, 1, 3, 8],
        )

    def test_empty_tree_traversal(self):
        empty_tree = BinarySearchTree()
        self.assertEqual(empty_tree.preorder(), [])
        self.assertEqual(empty_tree.inorder(), [])
        self.assertEqual(empty_tree.postorder(), [])
        self.assertEqual(empty_tree.reverse_preorder(), [])
        self.assertEqual(empty_tree.reverse_inorder(), [])
        self.assertEqual(empty_tree.reverse_postorder(), [])

    def test_single_node_tree(self):
        single_tree = BinarySearchTree()
        single_tree.insert(42)
        expected = [42]
        self.assertEqual(single_tree.preorder(), expected)
        self.assertEqual(single_tree.inorder(), expected)
        self.assertEqual(single_tree.postorder(), expected)
        self.assertEqual(single_tree.reverse_preorder(), expected)
        self.assertEqual(single_tree.reverse_inorder(), expected)
        self.assertEqual(single_tree.reverse_postorder(), expected)


if __name__ == "__main__":
    unittest.main()
