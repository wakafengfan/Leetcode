"""
198. House Robber


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

def house_rober_i(arr):
    n = len(arr)
    dp = [0] * (n + 2)

    for i in range(n-1, -1, -1):
        dp[i] = max(dp[i+1], arr[i] + dp[i+2])

    return dp[0]


print(house_rober_i([1,2,3,1]))





"""
213. House Robber II


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

def house_rober_ii(arr):
    n = len(arr)
    if n==1: return arr[0]

    memo = {}

    def dp(start, end):
        if (start, end) in memo:
            return memo[(start, end)]

        if start > end:
            return 0

        ans = max(dp(start+1, end), arr[start] + dp(start+2, end))

        memo[(start, end)] = ans

        return ans

    def dp2(start, end):
        dp_i_1, dp_i_2 = 0, 0
        for i in range(end, start-1, -1):
            dp_i = max(dp_i_1, arr[i]+dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i

    return max(dp2(0, n-2), dp2(1, n-1))


print(house_rober_ii([1,2,3,1]))
print(house_rober_ii([2,3,2]))
print(house_rober_ii([2]))



"""
337. House Robber III



The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
