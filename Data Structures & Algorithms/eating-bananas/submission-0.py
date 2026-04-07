import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        speed = 0
        while l <= r:
            midSpeed = (l+r)//2

            hour = 0
            for i in range(len(piles)):
                hour += math.ceil(piles[i]/midSpeed)
            
            if hour > h:
                l = midSpeed + 1
            elif hour <= h:
                speed = midSpeed
                r = midSpeed - 1
        return speed
