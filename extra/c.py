# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def get_values(root, stack):
    if root is not None:
        get_values(root.left, stack)
        stack.append(root.value)
        get_values(root.right, stack)


def solution(root):
    if root is None:
        return True
    stack_left = []
    get_values(root.left, stack_left)

    stack_right = []
    get_values(root.right, stack_right)
    return stack_left == stack_right[::-1]


# def test():
#     node1 = Node(3, None, None)
#     node2 = Node(4, None, None)
#     node3 = Node(4, None, None)
#     node4 = Node(3, None, None)
#     node5 = Node(2, node1, node2)
#     node6 = Node(2, node3, node4)
#     node7 = Node(1, node5, node6)
#     assert solution(node7)
