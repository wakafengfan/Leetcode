"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


"""


from typing import List


def combine_sum(candidates:List[int], target:int):
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
        # 剪枝
        if left_num < 0:
            break
        path.append(candidates[i])

        find_path(left_num, path, res, candidates, i, size)
        # print(f'2 - left_num:{left_num}, path:{path}, res:{res}, candidates:{candidates}, begin:{i}, size:{size}')
        # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除，
        path.pop()


# print(combine_sum([2,3,6,7], 7))


def t(arr, target):
    arr = sorted(arr)
    n = len(arr)
    res = []
    def backtrack(state, left_num, start):
        if left_num == 0:
            res.append(state.copy())
        else:
            for i in range(start, n):
                if arr[i] > left_num:
                    break
                state_copy = state.copy()
                state_copy.append(arr[i])
                backtrack(state_copy, left_num-arr[i], i)
                state_copy.remove(arr[i])
    backtrack([], target, 0)
    return res

print(t([2,3,6,7], 7))
print(t([2,3,5], 8))