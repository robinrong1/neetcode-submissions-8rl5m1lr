class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new = [0] * len(stones)
        for i in range(len(stones)):
            new[i] = stones[i] * -1
        
        heapq.heapify(new)

        while len(new) > 1:
            y = heapq.heappop(new)
            x = heapq.heappop(new)
            if x == y:
                continue
            else:
                #x < y
                heapq.heappush(new, y-x)
            
        if new:
            return -new[0]
        else:
            return 0
            


        