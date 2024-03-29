# Comment it before submitting
# from typing import Tuple


# class Node:
#     def __init__(self, left=None, right=None, value=0, size=0):
#         self.right = right
#         self.left = left
#         self.value = value
#         self.size = size


def size(node):
    if node is None:
        return 0
    return node.size


def split(root, k):
    if root is None:
        return None, None

    if size(root.left) >= k:
        root.size -= size(root.left)
        left, right = split(root.left, k)
        root.size += size(right)
        root.left = right
        return left, root

    k -= size(root) - size(root.right)
    root.size -= size(root.right)
    left, right = split(root.right, k)
    root.size += size(left)
    root.right = left
    return root, right


# def test():
#     node1 = Node(None, None, 3, 1)
#     node2 = Node(None, node1, 2, 2)
#     node3 = Node(None, None, 8, 1)
#     node4 = Node(None, None, 11, 1)
#     node5 = Node(node3, node4, 10, 3)
#     node6 = Node(node2, node5, 5, 6)
#     left, right = split(node6, 4)
#     assert left.size == 4
#     assert right.size == 2


# test()
