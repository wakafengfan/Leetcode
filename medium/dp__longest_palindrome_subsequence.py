"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


"""


import numpy as np


def longest_palindrome_subsequence(s):
    l = len(s)
    dp = np.zeros((l, l), dtype=int)

    for i in range(l):
        dp[i][i] = 1

    for i in range(l-1, -1, -1):
        for j in range(i+1, l):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    return dp[0][l-1]


print(longest_palindrome_subsequence('bbbab'))





