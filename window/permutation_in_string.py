"""

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


from collections import defaultdict


def permutation_in_string(s1, s2):
    n, m = len(s2), len(s1)
    left, right = 0, 0
    valid = 0
    needs, windows = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for c in s1:
        needs[c] += 1

    while right < n:
        c1 = s2[right]
        right += 1

        if c1 in needs:
            windows[c1] += 1
            if windows[c1] == needs[c1]:
                valid += 1

        while right - left >= m:
            c2 = s2[left]
            if valid == sum(needs.values()):
                return True

            left += 1
            if c2 in needs:
                if windows[c2] == needs[c2]:
                    valid -= 1
                windows[c2] -= 1
    return False



print(permutation_in_string("ab", "boac"))
