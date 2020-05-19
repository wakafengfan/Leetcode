"""


Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

def main_match(s, p):
    memo = {}

    def is_match(i, j):
        if (i,j) in memo:
            return memo[(i,j)]
        if j >= len(p): return i >= len(s)
        first_match = bool(s[i:]) and p[j] in [s[i], '.']
        if j < len(p) - 1 and p[j + 1] == '*':
            res = is_match(i, j+2) or (first_match and is_match(i+1, j))
        else:
            res = first_match and is_match(i+1, j+1)
        memo[(i,j)] = res
        return res

    return is_match(0, 0)

print(main_match("mississippi", "mis*is*p*."))
print(main_match("aab", "c*a*b"))
print(main_match("ab", ".*"))
print(main_match("aa", "a*"))




