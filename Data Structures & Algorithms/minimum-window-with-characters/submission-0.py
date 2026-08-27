class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashtable = {}
        ttable = {}
        if len(t) > len(s):
            return ""
        for c in t:
            ttable[c] = 1 + ttable.get(c,0)
        
        l= 0
        r = 0
        res = float('infinity')
        need = len(ttable)
        have = 0
        resArr = [-1]*2
        while r < len(s):

            hashtable[s[r]] = 1 + hashtable.get(s[r], 0)
            if s[r] in ttable and hashtable[s[r]] == ttable[s[r]]:
                have += 1
            
            while have == need:
                window = r-l+1
                if window < res:
                    resArr = [l,r]
                    res = window
                hashtable[s[l]] -= 1
                if s[l] in ttable and hashtable[s[l]] < ttable[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = resArr
        return s[l: r + 1] if res != float('infinity') else ""
            


