# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root):
    max_value = root.value

    for node in [root.left, root.right]:
        if node is not None:
            max_value = max(max_value, solution(node))

    return max_value


# def test():
#     node1 = Node(1)
#     node2 = Node(-5)
#     node3 = Node(3, node1, node2)
#     node4 = Node(2, node3, None)
#     assert solution(node4) == 3
