class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset= set(nums)
        maxLength = 0
        for num in hashset:
            if (num-1) not in hashset:
                length = 1
                while (num+1) in hashset:
                    length += 1
                    num += 1
                maxLength = max(maxLength, length)
        return maxLength