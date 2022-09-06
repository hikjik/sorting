from collections import Counter

input()
arr = input().split()
k = int(input())

for k, v in Counter(arr).most_common(k):
    print(k, end=" ")
