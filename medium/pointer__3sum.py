"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def three_sum(l):
    """
    排序之后，用双指针

    分治

    """

    l = sorted(l)
    res = []
    for i, num in enumerate(l[:len(l)-2]):
        left, right = i+1, len(l)-1
        while left < right:
            two_sum = l[left] + l[right]
            if two_sum == -num:
                res.append([num,l[left],l[right]])
                break
            elif two_sum > -num:
                right -= 1
            else:
                left += 1
    return res

print(three_sum([-1, 0, 1, 2, -1, -4]))
