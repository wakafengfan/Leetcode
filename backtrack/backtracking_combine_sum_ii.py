"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""

from typing import List


def combine_sum_ii(candidates:List[int], target:int):
    """


    :param candidates: list
    :param target:
    :return:
    """
    size = len(candidates)
    if size <= 0:
        return []

    # 先排序
    candidates.sort()

    path = []
    res = []

    # 递归
    find_path(target, path, res, candidates, 0, size)

    return res

def find_path(target, path, res, candidates, begin, size):
    if target == 0:
        res.append(path.copy())

    for i in range(begin, size):
        left_num = target - candidates[i]
        if left_num < 0:
            break
        path.append(candidates[i])
        # 当前数字如果和之前数同，则跳过，前一元素已遍历与之后元素的所有组合
        if i > begin and candidates[i] == candidates[i-1]:
            continue
        # 不能重用数字，每次遍历从下一个index开始
        find_path(left_num, path, res, candidates, i+1, size)
        # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除，
        path.pop()

print(combine_sum_ii([10,1,2,7,6,1,5], 8))
print(combine_sum_ii([2,5,2,1,2], 5))



def t(arr, target):
    arr = sorted(arr)
    n = len(arr)
    res = []
    def backtrack(state, left_num, start):
        if left_num == 0:
            res.append(state.copy())
        else:
            for i in range(start, n):
                if i > start and arr[i-1] == arr[i]:
                    continue
                if arr[i] > left_num:
                    break
                state_copy = state.copy()
                state_copy.append(arr[i])
                backtrack(state_copy, left_num-arr[i], i+1)
                state_copy.remove(arr[i])
    backtrack([], target, 0)
    return res

print(t([10,1,2,7,6,1,5], 8))
print(t([2,5,2,1,2], 5))