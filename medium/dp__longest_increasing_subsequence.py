"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""


def longest_increasing_subsequence(num):
    dp = [1] * len(num)
    all_max = 0

    dp[0] = 1
    for i in range(len(num)):
        for j in range(i):
            if num[i] > num[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                all_max = max(dp[i], all_max)
    return all_max


print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))



