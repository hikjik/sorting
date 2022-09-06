from collections import Counter

_ = input()
c = Counter(input())
for i in range(3):
    for j in range(c[f'{i}']):
        print(i, end=" ")
