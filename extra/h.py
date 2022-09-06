# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def get_sum(node, value):
    if node is None:
        return 0

    value = value * 10 + node.value
    if node.left is None and node.right is None:
        return value

    return get_sum(node.left, value) + get_sum(node.right, value)


def solution(root) -> int:
    return get_sum(root, 0)


# def test():
#     node1 = Node(2, None, None)
#     node2 = Node(1, None, None)
#     node3 = Node(3, node1, node2)
#     node4 = Node(2, None, None)
#     node5 = Node(1, node4, node3)
#     assert solution(node5) == 275


# test()
