class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(start):
            if start >= len(s):
                res.append(part.copy())
            

            for i in range(start, len(s)):
                if isPal(start, i):
                    part.append(s[start:i+1])
                    dfs(i+1)
                    part.pop()
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        dfs(0)
        return res


