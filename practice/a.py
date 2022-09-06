def gen(n: int, m: int, prefix: str) -> None:
    if n == 0 and m == 0:
        print(prefix)
        return

    if n > 0:
        gen(n - 1, m, prefix + "(")
    if m > 0 and n < m:
        gen(n, m - 1, prefix + ")")


n = int(input())
gen(n, n, "")
