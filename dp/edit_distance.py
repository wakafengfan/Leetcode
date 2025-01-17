"""

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""

import numpy as np
def edit_distance(word1, word2):
    n, m = len(word1), len(word2)
    dp = np.zeros((n+1, m+1), dtype=int)

    # base case
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                continue
            dp[i][j] = min(
                dp[i][j-1],  # 插入
                dp[i-1][j],  # 删除
                dp[i-1][j-1]  # 替换
            ) + 1

    return dp[n][m]

print(edit_distance("intention", "execution"))
