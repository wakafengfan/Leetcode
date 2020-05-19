"""


Maximum sum path in a matrix from top to bottom and back
Given a matrix of dimension N * M. The task is find the maximum sum of path from arr[0][0] to arr[N – 1][M – 1] and back from arr[N – 1][M – 1] to arr[0][0].

On the path from arr[0][0] to arr[N – 1][M – 1], you can traverse in down and right directions and on the path from arr[N – 1][M – 1] to arr[0][0], you can traverse in up and left directions.

Note: Both the path must not be equal i.e. there has to be at least one cell arr[i][j] which is not common in both the paths.



Examples:

Input:
mat[][]= {{1, 0, 3, -1},
          {3, 5, 1, -2},
          {-2, 0, 1, 1},
          {2, 1, -1, 1}}
Output: 16
maximum_sum_path
Maximum sum on path from arr[0][0] to arr[3][3]
= 1 + 3 + 5 + 1 + 1 + 1 + 1 = 13
Maximum sum on path from arr[3][3] to arr[0][0] = 3
Total path sum = 13 + 3 = 16

Input:
mat[][]= {{1, 0},
          {1, 1}}
Output: 3

https://www.geeksforgeeks.org/maximum-sum-path-in-a-matrix-from-top-to-bottom-and-back/

"""


def max_path(mat):
    n, m = len(mat), len(mat[0])
    # memo = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(n+1)]  # memo[n][m][n]
    memo = {}

    def sum_op(i1, j1, i2, j2):
        if i1 == i2 and j1 == j2:
            return mat[i1][j1]
        return mat[i1][j1] + mat[i2][j2]

    def dp(i1, j1, i2):
        if (i1, j1, i2) in memo:
            return memo[(i1, j1, i2)]

        j2 = i1 + j1 - i2

        # base case
        if i1 >= n or j1 >= m or i2 >= n or j2 >= m:
            return 0

        # ans = max(
        #     dp(i1 + 1, j1, i2 + 1),
        #     dp(i1, j1 + 1, i2),
        #     dp(i1 + 1, j1, i2),
        #     dp(i1, j1 + 1, i2 + 1)
        # ) + sum_op(i1, j1, i2, j2)

        all_down = dp(i1 + 1, j1, i2 + 1)
        all_right = dp(i1, j1 + 1, i2)
        right_down = dp(i1 + 1, j1, i2)
        down_right = dp(i1, j1 + 1, i2 + 1)

        ans = max(
            all_down,
            all_right,
            right_down,
            down_right
        ) + sum_op(i1, j1, i2, j2)

        memo[(i1, j1, i2)] = ans

        return ans

    res = dp(0, 0, 0)

    return res


print(max_path([[1, 0, 3, -1], [3, 5, 1, -2], [-2, 0, 1, 1], [2, 1, -1, 1]]))
