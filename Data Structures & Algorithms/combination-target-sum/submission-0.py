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

            dfs(i+1, remain-nums[i])
            
            combo.pop()
            dfs(i+1, remain)

        dfs(0, target)
        return res

