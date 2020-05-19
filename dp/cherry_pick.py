"""

In a N x N grid representing a field of cherries, each cell is one of three possible integers.



0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.


Your task is to collect maximum number of cherries possible by following the rules below:



Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.




Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

"""

import sys


def cherry_pick(grid):
    n = len(grid)
    # for i in range(n):
    #     for j in range(n):
    #         if grid[i][j] == -1:
    #             grid[i][j] = -sys.maxsize

    memo = {}

    def sum_op(i1, j1, i2, j2):
        if i1 == i2 and j1 == j2:
            return grid[i1][j1]
        return grid[i1][j1] + grid[i2][j2]

    def dp(i1, j1, i2):
        if (i1, j1, i2) in memo:
            return memo[(i1, j1, i2)]
        j2 = i1 + j1 - i2
        if i1 >= n or j1 >= n or i2 >= n or j2>=n:
            return 0

        # ans = -sys.maxsize
        # if grid[i1+1][j1] != -1 and grid[i2+1][j1] != -1:
        #     ans = max(ans, dp(i1+1, j1, i2+1))
        # if grid[i1][j1+1] != -1 and grid[i2][j2+1] != -1:
        #     ans = max(ans, dp(i1, j1+1, i2))
        # if grid[i1+1]

        ans = max(
            dp(i1 + 1, j1, i2 + 1),
            dp(i1, j1 + 1, i2),
            dp(i1 + 1, j1, i2),
            dp(i1, j1 + 1, i2 + 1)
        ) + sum_op(i1, j1, i2, j2)

        memo[(i1, j1, i2)] = ans

        return ans
    return dp(0,0,0)


print(cherry_pick([[0, 1, -1],
                   [1, 0, -1],
                   [1, 1, 1]]))
