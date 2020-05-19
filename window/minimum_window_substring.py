
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


"""

from collections import defaultdict
import sys
def minimum_window_substring(s, t):
    n, m = len(s), len(t)
    left, right = 0, 0
    valid = 0
    needs, windows = defaultdict(lambda: 0), defaultdict(lambda: 0)

    min_len = sys.maxsize

    for c in t:
        needs[c] += 1

    while right < n:
        c1 = s[right]
        right += 1

        if c1 in needs:
            windows[c1] += 1
            if windows[c1] == needs[c1]:
                valid += 1
        while valid >= sum(needs.values()):
            c2 = s[left]

            if right - left < min_len:
                start = left
                min_len = right-left

            left += 1
            if c2 in needs:
                if windows[c2] == needs[c2]:
                    valid -= 1
                windows[c2] -= 1

    return "" if min_len == sys.maxsize else s[start: start + min_len]


print(minimum_window_substring("ADOBECODEBANC", "ABC"))







