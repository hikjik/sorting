input()
arr = [int(i) for i in input().split()]

count = 0
expect_sum = 0
actual_sum = 0
for i, a in enumerate(arr):
    expect_sum += i
    actual_sum += a
    if actual_sum == expect_sum:
        count += 1
print(count)
