class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        #price to get to any airport
        for i in range(k + 1):
            #for each number of stops
            tempPrices = prices.copy()

            for s, d, p in flights:
                # scan through all possible flights, if the edge is infinity, that means we're not starting from that source yet, 
                if prices[s] == float('inf'):
                    continue
                
                #if its cheaper to fly from source to this node, we update
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
                
            prices = tempPrices
        return -1 if prices[dst] == float('inf') else prices[dst]