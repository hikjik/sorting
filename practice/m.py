import io
import os
import sys


def median(nums1, nums2) -> float:
    if len(nums1) > len(nums2):
        return median(nums2, nums1)

    left_half_size = (len(nums1) + len(nums2) + 1) // 2
    first_count_min, first_count_max = 0, len(nums1)
    while first_count_min <= first_count_max:
        first_count = (first_count_min + first_count_max) // 2
        second_count = left_half_size - first_count

        if first_count and nums1[first_count - 1] > nums2[second_count]:
            first_count_max = first_count - 1
        elif (
            first_count < len(nums1)
            and nums1[first_count] < nums2[second_count - 1]
        ):
            first_count_min = first_count + 1
        else:
            if not first_count:
                left_half_end = nums2[second_count - 1]
            elif not second_count:
                left_half_end = nums1[first_count - 1]
            else:
                left_half_end = max(
                    nums1[first_count - 1], nums2[second_count - 1]
                )
            if (len(nums1) + len(nums2)) % 2 == 1:
                return left_half_end * 1.0

            if first_count == len(nums1):
                right_half_start = nums2[second_count]
            elif second_count == len(nums2):
                right_half_start = nums1[first_count]
            else:
                right_half_start = min(nums1[first_count], nums2[second_count])
            return (left_half_end + right_half_start) / 2.0
    assert False, "Not reachable"


sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

input(), input()
nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]

sys.stdout.write(f"{median(nums1, nums2)}\n")
