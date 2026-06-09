from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        
        # 1. Sorting is mandatory for the duplicate-skipping logic to work
        nums.sort()
        
        def dfs(i, remain):
            # Base Case 1: Success!
            if remain == 0:
                res.append(combo.copy())
                return
            
            # Base Case 2: Out of bounds or current number is too large
            if i >= len(nums) or nums[i] > remain:
                return

            # --- CHOICE 1: Include nums[i] ---
            combo.append(nums[i])
            dfs(i, remain - nums[i]) # Move to next index
            combo.pop()                  # Backtrack

            # --- DUPLICATE SKIPPING ---
            # Advance 'i' past all elements that have the exact same value.
            # We do this because Choice 2 means "We are completely skipping this value
            # for this position", so we must skip all identical values too.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # --- CHOICE 2: Skip nums[i] (and all its duplicates) ---
            dfs(i+1, remain)

        dfs(0, target)
        return res