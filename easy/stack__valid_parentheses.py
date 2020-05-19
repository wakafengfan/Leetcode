mapper = {
    "(":")",
    "[":"]",
    "{":"}"
}
def valid_parentheses(s):
    """
    使用栈,遍历输入字符串

    如果当前字符为左半边括号时，则将其压入栈中

    如果遇到右半边括号时，分类讨论：

    1）如栈不为空且为对应的左半边括号，则取出栈顶元素，继续循环

    2）若此时栈为空，则直接返回false

    3）若不为对应的左半边括号，反之返回false

    https://github.com/azl397985856/leetcode/blob/master/problems/20.validParentheses.md

    """

    tmp_stack = []
    for c in s:
        if c in ['[','{','(']:
            tmp_stack.append(c)

        if c in [']','}',')']:
            if len(tmp_stack) == 0:
                return False
            if mapper[tmp_stack[-1]] == c:
                tmp_stack.pop()
            else:
                return False

    return True

print(valid_parentheses('{[]}'))


s1 = '(())'
s = '(()))'

def t(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True


print(t(s))


"""
时间复杂度：O(n)
空间复杂度：O(1)

"""

def t1(s):
    stack = 0
    cnt = 0

    for c in s:
        if c == '(':
            stack += 1
        else:
            if stack == 0:
                print(cnt * 2)
                return False
            else:
                stack -= 1
                cnt += 1
    print(cnt * 2)
    return True


print(t1(s))