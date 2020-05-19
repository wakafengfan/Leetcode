"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.


"""



def jump_game(nums):

    _len = len(nums)
    _max = 1

    for i in range(_len-1):
        if _max < i:
            return False
        _max = max(_max, nums[i] + i)

    return _max >= _len-1

print(jump_game([3,2,1,0,4]))



def t(arr):
    n = len(arr)
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    for i in range(n):
        if dp[i-1] >= i and i < n-1:
            dp[i] = i + arr[i]
        if dp[i-1] < i:
            return False
        if dp[i] >= n-1:
            return True

print(jump_game([2,3,1,1,4]))
print(jump_game([3,2,1,0,4]))
