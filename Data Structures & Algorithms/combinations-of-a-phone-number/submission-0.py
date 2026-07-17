class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        part = []
        def dfs(i):
            if len(part) == len(digits):
                res.append("".join(part.copy()))
                return
            
            for c in mapping[digits[i]]:
                part.append(c)
                dfs(i + 1)
                part.pop()




        if digits:
            dfs(0)
        return res