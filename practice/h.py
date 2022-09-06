from functools import cmp_to_key


def _comp(lhs, rhs):
    if len(lhs) == len(rhs):
        return lhs < rhs
    return lhs + rhs < rhs + lhs


def comp(lhs, rhs):
    return 1 - 2 * _comp(lhs, rhs)


input()
nums = input().split()

nums.sort(key=cmp_to_key(comp), reverse=True)
print("".join(nums))
