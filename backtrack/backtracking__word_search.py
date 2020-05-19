"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


"""


def word_search(board, word):
    m, n = len(board), len(board[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = []

    def backtrack(w, p, left_directions):
        if len(w) <= 0:
            res.append(p)
        else:

            for d in left_directions:
                x, y = p[-1][0] + d[0], p[-1][1] + d[1]
                if 0 <= x < m and 0 <= y < n and (x, y) not in p and board[x][y] == w[0]:
                    p.append((x, y))
                    backtrack(w[1:], p, [_ for _ in directions if _ != (-d[0], -d[1])])
                    p.remove((x, y))

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                backtrack(word[1:], [(i, j)], directions)

    return True if len(res) > 0 else False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(word_search(board, "ABCCED"))
print(word_search(board, "SEE"))
print(word_search(board, "ABCB"))