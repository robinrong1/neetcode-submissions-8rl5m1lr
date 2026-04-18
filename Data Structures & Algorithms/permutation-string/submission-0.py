class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map = {}
        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
        s2Map = {}
        for j in range(len(s1)):
            s2Map[s2[j]] = 1 + s2Map.get(s2[j], 0)
        l, r = 0, len(s1)-1
        while r < len(s2):
            if s1Map == s2Map:
                return True
            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                del s2Map[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)
        
        return False
                    