def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] >= x:
            r = m
        else:
            l = m + 1
    return l + 1 if l < len(arr) else -1


input()
arr = [int(i) for i in input().split()]
price = int(input())

print(lower_bound(arr, price), lower_bound(arr, 2 * price))
