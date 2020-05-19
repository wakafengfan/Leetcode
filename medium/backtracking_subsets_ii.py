"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""


def subsets_ii(nums):
    res = []
    tmp = []

    def backtrack(res, tmp, n, start):
        res.append(tmp.copy())
        for i in range(start, len(n)):
            if i>start and n[i-1] == n[i]:
                continue
            tmp.append(n[i])
            backtrack(res, tmp, n, i+1)
            tmp.pop(-1)
    backtrack(res, tmp, nums, 0)
    return res

print(subsets_ii([1,2,2]))
