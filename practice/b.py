SYMBOLS = [
    list(x)
    for x in ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
]


def gen(lst, prefix):
    if not lst:
        print(prefix, end=" ")
        return
    for i in SYMBOLS[lst[0]]:
        gen(lst[1:], prefix + i)


a = [int(i) for i in input()]
gen(a, "")
