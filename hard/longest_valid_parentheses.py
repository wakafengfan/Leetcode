"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""

def longest_valid_parentheses(s):
    stack = 0
    cnt = 0
    max_s = 0

    for c in s:
        if c == '(':
            stack += 1
        else:
            if stack == 0:
                max_s = max(max_s, cnt*2)
                cnt = 0
            else:
                stack -= 1
                cnt += 1
    max_s = max(max_s, cnt * 2)
    return max_s

s = ')()())'

print(longest_valid_parentheses(s))
