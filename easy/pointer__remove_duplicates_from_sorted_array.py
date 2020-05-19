"""
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.



Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.


"""

def remove_duplicates(arr):
    """
    使用快慢指针来记录遍历的坐标。

    开始时这两个指针都指向第一个数字

    如果两个指针指的数字相同，则快指针向前走一步

    如果不同，则两个指针都向前走一步

    当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数

    https://github.com/azl397985856/leetcode/blob/master/problems/26.remove-duplicates-from-sorted-array.md

    """
    if not arr:
        return 0

    pre = 0
    for cur in range(len(arr)):
        if arr[pre] != arr[cur]:
            pre += 1
            arr[pre] = arr[cur]

    return pre + 1
