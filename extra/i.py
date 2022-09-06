def count_bst(n):
    T = [1, 1]
    while len(T) <= n:
        s = 0
        for i in range(len(T)):
            s += T[i] * T[len(T) - i - 1]
        T.append(s)
    return T[n]


n = int(input())
print(count_bst(n))