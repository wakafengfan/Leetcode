"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


def next_permutation(nums):
    """
    1.从后往前，找到第一个下降点
    2.从后往前，找到第一个比下降点大的数，交换位置
    3.重新排列下降点之后的数字

    为了使增量最小，其实剩下的元素从左到右是递减的，而我们想要变成递增的，我们只需要不断交换首尾元素即可

    写几个例子通常会帮助理解问题的规律
    在有序数组中首尾指针不断交换位置即可实现reverse
    找到从右边起第一个大于nums[i]的，并将其和nums[i]进行交换

    :param nums: list
    :return:
    """

    down_index = None
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            down_index = i
            break
    if not down_index:
        nums.reverse()
    else:
        for i in range(len(nums)-1, i, -1):
            if nums[down_index] < nums[i]:
                nums[down_index], nums[i] = nums[i], nums[down_index]
                break
        i, j = down_index+1, len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    return nums

print(next_permutation([3,5,1,4,2]))


