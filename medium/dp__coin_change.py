"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


"""

import numpy as np
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(amount + 1):
        for coin in coins:
            if i-coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])

    return -1 if dp[amount] == amount + 1 else dp[amount]


print(coin_change([1, 2, 5], 11))








