"""

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
def permutation(l):
    res = []

    def backtrace(nums, pre_list):
        if len(nums) <= 0:
            res.append(pre_list)
        else:
            for i in nums:
                pre_list_copy = pre_list.copy()
                pre_list_copy.append(i)

                left_num = nums.copy()
                left_num.remove(i)

                backtrace(left_num, pre_list_copy)
    backtrace(l, [])

    return res

# print(permutation([1,2,3]))


def t(nums):
    res = []

    def backtrack(path, nums_):
        if len(nums_) == 0:
            res.append(path)
        else:
            for n in nums_:
                path.append(n)
                backtrack(path.copy(), [_ for _ in nums_ if _!=n])
                path.remove(n)

    backtrack([], nums)
    return res


print(t([1,2,3]))