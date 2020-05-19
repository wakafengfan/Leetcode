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


"""

"""


"""

class Solution(object):
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):  # 翻转遍历
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():  # 加载操作数情况：如果遇到最后一位 或者前一位是符号 则
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':  # 加载操作符情况：
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':  # 遇到左括号 需要做一次运算
                    self.compute(operands, operators)
                operators.pop()

        while operators:  # 遍历符号集合
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()  # operands吐出来两个运算，吞进去一个结果
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)