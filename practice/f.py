def max_perimeter(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if arr[i] < arr[i + 1] + arr[i + 2]:
            return arr[i] + arr[i + 1] + arr[i + 2]


input()
nums = [int(i) for i in input().split()]
print(max_perimeter(nums))
