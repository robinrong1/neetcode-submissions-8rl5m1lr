class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}

        for i in range(len(s)):
            frequency[s[i]] = frequency.get(s[i],0) + 1
        
        for i in range(len(t)):
            if t[i] in frequency:
                frequency[t[i]] = frequency[t[i]] - 1
            else:
                return False
        for lettere in frequency:
            if frequency[lettere] != 0:
                return False
        return True