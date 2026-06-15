#Stack : Reverse Polish Notation

"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens)>1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a+ b
                    elif tokens[i] == '-':
                        result = a-b
                    elif tokens[i] == '*':
                        result a * b
                    elif tokens[i] == '/':
                        result = int(a/b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])