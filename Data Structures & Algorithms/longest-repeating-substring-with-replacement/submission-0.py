class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0

        tol = 0
        hashMap = {}
        max_f = 0
        while r < len(s):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            max_f = max(hashMap[s[r]], max_f)

            while ((r - l + 1) - max_f) > k:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res   

