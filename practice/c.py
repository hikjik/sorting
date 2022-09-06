import sys


def count(seq):
    count = 0
    for symbol in seq:
        while True:
            s = sys.stdin.read(1)
            if symbol == s:
                count += 1
                break
            elif s.isspace():
                return count
    return count


seq = input()
print(count(seq) == len(seq))
