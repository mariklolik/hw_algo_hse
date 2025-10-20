from homework_4.tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return self.root

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return current.left
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return current.right
                current = current.right

    def _traverse(self, node, order):
        if node is None:
            return

        if order == "pre":
            yield node.value
            yield from self._traverse(node.left, order)
            yield from self._traverse(node.right, order)
        elif order == "in":
            yield from self._traverse(node.left, order)
            yield node.value
            yield from self._traverse(node.right, order)
        elif order == "post":
            yield from self._traverse(node.left, order)
            yield from self._traverse(node.right, order)
            yield node.value
        elif order == "rev_pre":
            yield node.value
            yield from self._traverse(node.right, order)
            yield from self._traverse(node.left, order)
        elif order == "rev_in":
            yield from self._traverse(node.right, order)
            yield node.value
            yield from self._traverse(node.left, order)
        elif order == "rev_post":
            yield from self._traverse(node.right, order)
            yield from self._traverse(node.left, order)
            yield node.value
        else:
            raise ValueError(f"Unknown traversal order: {order}")

    def preorder(self):
        return list(self._traverse(self.root, "pre"))

    def inorder(self):
        return list(self._traverse(self.root, "in"))

    def postorder(self):
        return list(self._traverse(self.root, "post"))

    def reverse_preorder(self):
        return list(self._traverse(self.root, "rev_pre"))

    def reverse_inorder(self):
        return list(self._traverse(self.root, "rev_in"))

    def reverse_postorder(self):
        return list(self._traverse(self.root, "rev_post"))
