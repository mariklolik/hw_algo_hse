from homework_4.tree_node import TreeNode


def is_balanced(root: TreeNode) -> bool:
    def check(node):
        if node is None:
            return 0, True

        left_height, left_balanced = check(node.left)
        if not left_balanced:
            return 0, False

        right_height, right_balanced = check(node.right)
        if not right_balanced:
            return 0, False

        balanced = abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1
        return height, balanced

    _, balanced = check(root)
    return balanced
