# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def is_balance_tree(root):
    if root is None:
        return True, 0

    is_left_balance, depth_left = is_balance_tree(root.left)
    is_right_balance, depth_right = is_balance_tree(root.right)

    is_balance = (
        is_left_balance
        and is_right_balance
        and abs(depth_left - depth_right) <= 1
    )
    depth = 1 + max(depth_left, depth_right)

    return is_balance, depth


def solution(root):
    is_balance, _ = is_balance_tree(root)
    return is_balance


# def test():
#     node1 = Node(1)
#     node2 = Node(-5)
#     node3 = Node(3, node1, node2)
#     node4 = Node(10)
#     node5 = Node(2, node3, node4)
#     assert solution(node5)
