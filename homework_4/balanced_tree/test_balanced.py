import unittest

from homework_4.tree_node import TreeNode
from homework_4.balanced_tree.balanced import is_balanced


class TestBalancedTree(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

    def test_single_node(self):
        self.assertTrue(is_balanced(TreeNode(10)))

    def test_balanced_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertTrue(is_balanced(root))

    def test_unbalanced_tree_left_heavy(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertFalse(is_balanced(root))

    def test_unbalanced_tree_right_heavy(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertFalse(is_balanced(root))

    def test_balanced_after_insertions(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertTrue(is_balanced(root))

    def test_almost_balanced_but_not_quite(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.right = TreeNode(2)
        self.assertFalse(is_balanced(root))

    def test_balanced_with_null_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        self.assertTrue(is_balanced(root))


if __name__ == "__main__":
    unittest.main()
