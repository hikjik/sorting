n = int(input())
nums = [int(i) for i in input().split()]


def is_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


for _ in range(n):
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(*nums)
    if is_sorted(nums):
        break
