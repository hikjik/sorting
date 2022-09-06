# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


INF = 10**9


def solution(root) -> int:
    max_sum = -INF

    def find_max_sum(node):
        if node is None:
            return 0

        left_max = find_max_sum(node.left)
        right_max = find_max_sum(node.right)

        nonlocal max_sum
        max_sum = max(
            max_sum,
            node.value,
            left_max + node.value,
            node.value + right_max,
            left_max + node.value + right_max,
        )
        return max(
            left_max + node.value,
            node.value + right_max,
            node.value,
        )

    find_max_sum(root)
    return max_sum


# def test():
#     node1 = Node(5, None, None)
#     node2 = Node(1, None, None)
#     node3 = Node(-3, node2, node1)
#     node4 = Node(2, None, None)
#     node5 = Node(2, node4, node3)
#     assert solution(node5) == 6


# test()
