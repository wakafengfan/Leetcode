"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


"""

"""
先求不重叠的区间有几个，再从总区间数中减去得到重叠的区间数

"""



def non_overlapping(nums):
    count = 1
    nums = sorted(nums, key=lambda x: x[1])
    start, end = nums[0][0], nums[0][1]

    for s, e in nums:
        if s >= end:
            count += 1
            end = e
    return len(nums) - count


print(non_overlapping([[1,2],[2,3],[3,4],[1,3]]))

