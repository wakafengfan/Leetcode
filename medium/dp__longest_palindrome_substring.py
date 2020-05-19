"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad" 输出: "bab" 注意: "aba" 也是一个有效答案。 示例 2：

输入: "cbbd" 输出: "bb"


"""

def longest_palindrome_substring(s):
    """

    :param s:
    :return:
    """
    res = s[0]
    import numpy as np
    dp = np.zeros((len(s), len(s)))
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if i == j:  # 一个字符
                dp[i][j] = True
            elif j - i == 1 and s[j] == s[i]:  # 两个相同字符
                dp[i][j] = True

            elif s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True

            if dp[i][j] and j-i+1>len(res):  # 当前i到j是回文，记录之间的字符
                res = s[i:j+1]

    return res
print(longest_palindrome_substring('babad'))


def find_max_set(arr):
    x_arr, y_arr = zip(*arr)
    max_x, max_y = max(x_arr), max(y_arr)
    def func(x_):
        return - max_y * x_ / max_x + max_y
    arr_ = [[i, j] for i, j in arr if j >= func(i)]
    res = []
    for i, j in arr_:
        flag = True
        for i_, j_ in arr_:
            if i_ > i and j_ > j:
                flag = False
                break
        if flag:
            res.append([i,j])

    return res

if __name__ == '__main__':
    arr = [[1,2],[5,3],[4,6],[7,5],[9,0]]
    r = find_max_set(arr)
    for i, j in r:
        print(f'{i} {j}')
    import sys
    sys.argv[1]