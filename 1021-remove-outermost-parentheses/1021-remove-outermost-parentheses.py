class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        bal = 0
        start = 0

        for i, char in enumerate(s):
            if char == '(':
                if bal == 0:
                    start = i
                bal += 1
            elif char == ')':
                bal -= 1
                if bal == 0:
                    result.append(s[start+1:i])

        return "".join(result)