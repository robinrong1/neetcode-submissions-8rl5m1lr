class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            else:
                record.add(nums[i])
        return False