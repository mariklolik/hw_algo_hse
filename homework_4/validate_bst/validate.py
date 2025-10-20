from homework_4.tree_node import TreeNode


def is_bst(root: TreeNode) -> bool:
    def helper(node, min_value, max_value):
        if node is None:
            return True

        value = node.value
        if min_value is not None and value <= min_value:
            return False
        if max_value is not None and value >= max_value:
            return False

        return helper(node.left, min_value, value) and helper(node.right, value, max_value)

    return helper(root, None, None)
