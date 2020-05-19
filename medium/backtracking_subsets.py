"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
from typing import List


def subsets(nums):
    res = []
    tmp = []

    def backtrack(res:List[int], tmp:List[int], n, start):
        res.append(tmp.copy())

        for i in range(start, len(n)):
            tmp.append(n[i])
            backtrack(res, tmp, n, i+1)
            tmp.pop(-1)

    backtrack(res, tmp, nums, 0)
    return res

print(subsets([1,2,3]))


