import unittest

from homework_4.tree_node import TreeNode
from homework_4.validate_bst.validate import is_bst


class TestValidateBST(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_bst(None))

    def test_single_node(self):
        self.assertTrue(is_bst(TreeNode(42)))

    def test_valid_bst(self):
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)
        self.assertTrue(is_bst(root))

    def test_invalid_bst_due_to_left_child(self):
        root = TreeNode(5)
        root.left = TreeNode(7)
        root.right = TreeNode(8)
        self.assertFalse(is_bst(root))

    def test_invalid_bst_due_to_right_child(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(4)
        self.assertFalse(is_bst(root))

    def test_invalid_bst_due_to_subtree_on_left(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.right = TreeNode(12)
        self.assertFalse(is_bst(root))

    def test_invalid_bst_due_to_subtree_on_right(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        self.assertFalse(is_bst(root))

    def test_duplicate_values(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        root.right.left = TreeNode(5)
        self.assertFalse(is_bst(root))

    def test_skewed_bst(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertTrue(is_bst(root))


if __name__ == "__main__":
    unittest.main()
