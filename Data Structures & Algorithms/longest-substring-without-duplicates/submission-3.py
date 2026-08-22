class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        while r < len(s):
            chars = set()
            l = r
            while r < len(s):
                if s[r] in chars:
                    break
                else:
                    chars.add(s[r])
                    r += 1
                res = max(res, r -l)
        return res