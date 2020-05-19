"""
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


# def longest_substring(s):
#     """
#     用字典记录每个字上次出现的位置
#
#     主要与窗口的左边界比较，在边界外ok，不用动边界，在边界内需要截断形成新边界
#
#     """
#     res, left = 0, 0
#     lookup = {}
#     for right in range(len(s)):
#         if s[right] in lookup:
#             left = max(left, lookup[s[right]]+1)
#         lookup[s[right]] = right
#         res = max(res, right-left+1)
#
#     return res


from collections import defaultdict
import sys
def longest_substring_no_repeat(s):
    n = len(s)
    left, right = 0, 0
    windows = defaultdict(lambda: 0)

    max_len = -sys.maxsize
    while right < n:
        c1 = s[right]
        right += 1

        windows[c1] += 1

        while windows[c1] > 1:
            c2 = s[left]
            left += 1

            windows[c2] -= 1

        if right-left > max_len:
            max_len = right-left
            start = left

    return s[start: start + max_len]


print(longest_substring_no_repeat("pwwkew"))


