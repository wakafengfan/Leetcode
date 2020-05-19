"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.


你和你的朋友面前有一排石头堆，用一个数组 piles 表示，piles[i] 表示第 i 堆石子有多少个。你们轮流拿石头，一次拿一堆，但是只能拿走最左边或者最右边的石头堆。所有石头被拿完后，谁拥有的石头多，谁获胜。
石头的堆数可以是任意正整数，石头的总数也可以是任意正整数，这样就能打破先手必胜的局面了。比如有三堆石头 piles = [1, 100, 3]，先手不管拿 1 还是 3，能够决定胜负的 100 都会被后手拿走，后手会获胜。
假设两人都很聪明，请你设计一个算法，返回先手和后手的最后得分（石头总数）之差。比如上面那个例子，先手能获得 4 分，后手会获得 100 分，你的算法应该返回 -96。

piles = [3, 9, 1, 2]

"""

import numpy as np
class Pair(object):
    def __init__(self, fir, sec):
        self.fir = fir
        self.sec = sec



def stone_game(piles):
    n = len(piles)

    # 1.初始化数组 & 2.base case
    dp = []
    for i in range(n):
        dp.append([0] * n)

    # 记录：dp = [[0] * n] * n -> list * n 每个list还是指向同一个地址

    for i in range(n):
        for j in range(n):
            dp[i][j] = Pair(0, 0)

    ### debug ###
    # for i_ in range(n):
    #     tmp = []
    #     for j_ in range(n):
    #         tmp.append((dp[i_][j_].fir, dp[i_][j_].sec))
    #     print(tmp)
    ### debug ###

    for i in range(n):
        dp[i][i].fir = piles[i]
        dp[i][i].sec = 0

    # 3.斜着遍历数组
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = l + i - 1
            left = piles[i] + dp[i+1][j].sec
            right = piles[j] + dp[i][j-1].sec

            if left > right:
                dp[i][j].fir = left
                dp[i][j].sec = dp[i+1][j].fir
            else:
                dp[i][j].fir = right
                dp[i][j].sec = dp[i][j-1].fir

            ### debug ###
            # for i in range(n):
            #     tmp = []
            #     for j in range(n):
            #         tmp.append((dp[i][j].fir, dp[i][j].sec))
            #     print(tmp)
            ### debug ###

    return dp[0][n-1].fir - dp[0][n-1].sec

print(stone_game([3,9,1,2]))








