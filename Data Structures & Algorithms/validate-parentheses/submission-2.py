class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c not in parentheses:
                stack.append(c)
            else:
                if not stack or stack.pop() != parentheses[c]:
                        return False
                
        return not stack