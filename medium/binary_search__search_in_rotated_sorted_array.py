"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


"""


def search_in_rotated_sorted_array(arr, target):
    """
    假如mid小于start，则mid一定在右边有序部分。 假如mid大于等于start， 则mid一定在左边有序部分。

    注意等号的考虑

    然后我们继续判断target在哪一部分， 我们就可以舍弃另一部分了

    :param arr:
    :return:
    """

    left, right = 0, len(arr)-1
    while left < right:
        mid = (right-left)//2 + left

        if arr[mid] == target:
            return mid

        # mid在左侧有序
        if arr[mid] > arr[left]:
            # target在有序序列
            if arr[left] <= target <= arr[mid]:
                right = mid
            else:
                left = mid + 1

        # mid在右侧有序
        else:
            # target在有序序列
            if arr[mid] <= target <= arr[right]:
                left = mid
            else:
                right = mid -1

    return -1


print(search_in_rotated_sorted_array([4,5,6,7,0,1,2], 3))

