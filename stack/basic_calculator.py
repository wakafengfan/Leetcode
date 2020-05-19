"""

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""

# 字符转整数
def str2int(s):
    num = 0
    for i, c in enumerate(s[::-1]):
        num += 10 ** i * int(c)
    return num

# print(str2int('12345'))

def is_digit(c):
    try:
        c = int(c)
        return True
    except Exception:
        return False


def basic_calculator(s):

    def helper(s):
        stack = []
        num = 0
        sign = '+'
        while len(s) > 0:
            c = s.pop(0)
            if is_digit(c):
                num = num * 10 + int(c)

            if c == '(':
                num = helper(s)

            if (not is_digit(c) and c != ' ') or len(s) == 0:
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = stack[-1] / float(num)

                sign = c
                num = 0

            if c == ')':
                break
        return sum(stack)

    return helper(list(s))

print(basic_calculator('(1+(4+5+2)-3)+(6+8)'))


