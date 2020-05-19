"""

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

"""


def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    res = []

    def backtrack(board, row):
        if row >= n:
            res.append([''.join(r) for r in board])
        else:

            for i in range(n):
                if not is_valid(board, row, i):
                    continue
                board[row][i] = 'Q'
                backtrack(board, row+1)
                board[row][i] = '.'
    backtrack(board, 0)
    return res


def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    if row > 0 and col > 0 and board[row-1][col-1] == 'Q':
        return False
    if row > 0 and col < len(board[0])-1 and board[row-1][col+1] == 'Q':
        return False
    return True



print(n_queens(4))