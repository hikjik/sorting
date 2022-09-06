def sift_down(heap, idx):
    left_idx = 2 * idx
    right_idx = 2 * idx + 1

    max_value = heap[idx]

    left = None
    if left_idx < len(heap):
        left = heap[left_idx]
        max_value = max(max_value, left)

    right = None
    if right_idx < len(heap):
        right = heap[right_idx]
        max_value = max(max_value, right)

    if max_value == heap[idx]:
        return idx

    if left is not None and max_value == left:
        heap[idx], heap[left_idx] = heap[left_idx], heap[idx]
        return sift_down(heap, left_idx)

    if right is not None and max_value == right:
        heap[idx], heap[right_idx] = heap[right_idx], heap[idx]
        return sift_down(heap, right_idx)
    return idx


# def test():
#     sample = [-1, 12, 1, 8, 3, 4, 7]
#     assert sift_down(sample, 2) == 5
# test()