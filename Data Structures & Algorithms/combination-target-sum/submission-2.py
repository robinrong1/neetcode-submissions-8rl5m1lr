from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        nums.sort()

        def dfs(i, remain):

            if remain == 0:
                res.append(combo.copy())
                return
            if i >= len(nums) or nums[i] > remain:
                return
            
            combo.append(nums[i])
            dfs(i, remain-nums[i])

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            combo.pop()
            dfs(i+1, remain)
        dfs(0, target)
        return res
