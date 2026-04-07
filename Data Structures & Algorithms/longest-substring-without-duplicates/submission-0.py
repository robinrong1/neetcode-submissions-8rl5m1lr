class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        charSet = set()
        while r < len(s):
            while s[r] in charSet:
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res