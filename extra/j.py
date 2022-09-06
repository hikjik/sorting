from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def insert(root, key):
    if root is None:
        return Node(value=key)

    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# def test():
#     node1 = Node(None, None, 7)
#     node2 = Node(node1, None, 8)
#     node3 = Node(None, node2, 7)
#     new_head = insert(node3, 6)
#     assert new_head is node3
#     assert new_head.left.value == 6
# test()
