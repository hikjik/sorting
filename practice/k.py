def _merge(lhs, rhs):
    i, j = 0, 0
    arr = []
    while i < len(lhs) or j < len(rhs):
        if j == len(rhs) or i < len(lhs) and lhs[i] < rhs[j]:
            arr.append(lhs[i])
            i += 1
        else:
            arr.append(rhs[j])
            j += 1
    return arr


def merge(arr, lf, mid, rg):
    return _merge(arr[lf:mid], arr[mid:rg])


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return

    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    merged = merge(arr, lf, mid, rg)
    for i in range(lf, rg):
        arr[i] = merged[i - lf]
