"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""

import sys


def maximum_subarray_(arr):
    max_sum = -sys.maxsize
    for i in range(len(arr)):
        tmp = 0
        for j in range(i, len(arr)):
            tmp += arr[j]
            max_sum = max(max_sum, tmp)

    return max_sum


def maximum_subarray(arr):
    d = [-sys.maxsize] * len(arr)
    d[0] = arr[0]
    all_max = arr[0]

    for i in range(1, len(arr)):
        d[i] = max(d[i-1] + arr[i], arr[i])
        all_max = max(d[i], all_max)
    return all_max


print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))

