import io
import os
import sys


sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())

arr.sort()


def count_pairs(arr, distance):
    count = 0
    l, r = 0, 0
    while l < len(arr) or r < len(arr):
        while r < len(arr) and arr[r] <= arr[l] + distance:
            r += 1
        count += r - l - 1
        l += 1
    return count


left, right = 0, arr[-1] - arr[0]
while left < right:
    mid = (left + right) // 2
    count = count_pairs(arr, mid)

    if count < k:
        left = mid + 1
    else:
        right = mid

print(left)
