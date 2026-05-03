class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {')': '(',
                    '}': '{',
                    ']': '['}

        stack = []

        for c in s:
            if stack and c in brackets and stack[-1] == brackets[c]:
                stack.pop()
            else:
                stack.append(c)

        return False if stack else True
                

        