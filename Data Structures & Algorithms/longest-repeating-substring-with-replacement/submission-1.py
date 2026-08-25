class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        max_f = 0

        sofar = 0
        chars = {}
        while r < len(s):
            chars[s[r]] = 1 + chars.get(s[r],0)
            max_f = max(chars[s[r]], max_f)

            while ((r-l) + 1 - max_f) > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)


            r += 1
        return res