"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49


"""


"""
思路：

假如左侧的线段高度比右侧的高度低，那么我们通过左移右指针来将长度缩短为n-1的做法是没有意义的， 因为新的形成的面积变成了(n-1) * heightOfLeft 
这个面积一定比刚才的长度为n的面积n * heightOfLeft 小

也就是说最大面积一定是当前的面积或者通过移动短的线段得到

"""


def container_with_most_water(l):
    left, right = 0, len(l)-1
    max_area = 0
    while left < right:
        current_area = abs(left - right) * min(l[left], l[right])
        max_area = max(current_area, max_area)
        if l[left] < l[right-1]:
            left+=1
        else:
            right-=1
    return max_area

print(container_with_most_water([1,8,6,2,5,4,8,3,7]))


