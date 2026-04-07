class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxHeight = 0
        while l < r:

            maxHeight = max(maxHeight, min(heights[l], heights[r]) * (r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxHeight