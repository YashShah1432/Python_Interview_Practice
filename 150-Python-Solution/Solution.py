class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        operator = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b,
            '/' : lambda a, b : int(a / b)
        }
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                s.append(int(token))
            else:
                first = s.pop()
                second = s.pop()
                result = operator[token](second, first)
                s.append(result)
        return s[0]