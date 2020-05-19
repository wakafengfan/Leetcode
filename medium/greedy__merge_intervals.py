"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""


from typing import List


def merge_intervals(intervals: List[List]):
    """
    先排序

    """
    intervals.sort(key=lambda x: x[0])

    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][1] <= res[-1][1]:
            res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
        else:
            res.append(intervals[i])

    return res

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

