# 70015119

from typing import List, Tuple


def broken_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        if nums[middle] < target:
            if nums[middle] < nums[left] <= target:
                right = middle - 1
            else:
                left = middle + 1

        else:
            if target <= nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def read_input() -> Tuple[List[int], int]:
    input()
    nums = [int(i) for i in input().split()]
    target = int(input())
    return nums, target


if __name__ == "__main__":
    nums, target = read_input()
    print(broken_search(nums, target))
