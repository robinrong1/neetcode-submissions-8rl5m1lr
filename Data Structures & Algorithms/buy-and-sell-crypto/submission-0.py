class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if lower than current min, go to there

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            profit = max(profit, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
            
            r += 1
        return profit