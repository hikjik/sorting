# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def is_search_tree(root):
    if root is None:
        return True, None

    max_value = root.value

    if root.right is not None:
        is_right, right_max = is_search_tree(root.right)
        if not is_right or right_max <= root.value:
            return False, None
        max_value = max(max_value, right_max)

    if root.left is not None:
        is_left, left_max = is_search_tree(root.left)
        if not is_left or left_max >= root.value:
            return False, None
        max_value = max(max_value, left_max)

    return True, max_value


def solution(root) -> bool:
    ok, _ = is_search_tree(root)
    return ok


# def test():
#     node1 = Node(1, None, None)
#     node2 = Node(4, None, None)
#     node3 = Node(3, node1, node2)
#     node4 = Node(8, None, None)
#     node5 = Node(5, node3, node4)

#     assert solution(node5)
#     node2.value = 5
#     assert not solution(node5)
