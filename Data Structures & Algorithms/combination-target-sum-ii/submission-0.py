class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        candidates.sort()
        
        def dfs(i, remain):

            if remain == 0:
                res.append(combo.copy())
                return
            
            if i >= len(candidates) or remain < 0:
                return
            #use it
            combo.append(candidates[i])
            dfs(i+1, remain-candidates[i])
            #dont 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            combo.pop()
            dfs(i+1, remain)

            
        dfs(0, target)
        return res