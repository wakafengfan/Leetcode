"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


"""

from typing import List


def permutation_ii(nums_: List[int]):
    nums_.sort()
    res = []

    def backtrace(nums, pre_list):
        if len(nums) <= 0:
            res.append(pre_list)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                p_list = pre_list.copy()
                p_list.append(nums[i])

                left_num = nums.copy()
                left_num.pop(i)
                backtrace(left_num, p_list)

    backtrace(nums_, [])

    return res

# print(permutation_ii([1,1,2]))




def t(l):
    res = []

    def backtrack(path, nums_):
        if len(nums_) == 0:
            res.append(path)
        else:
            for i, n in enumerate(nums_):
                if i > 0 and nums_[i] == nums_[i-1]:
                    continue
                path.append(n)
                backtrack(path.copy(), nums_[:i] + nums_[i+1:])
                path.remove(n)
    backtrack([], l)

    return res

print(t([1,1,2]))

