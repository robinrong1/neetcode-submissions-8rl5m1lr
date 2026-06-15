class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        theHeap = []
        res = []
        for i in range(len(points)):
            theHeap.append((((points[i][0]**2)+ (points[i][1]**2)),i))
        heapq.heapify(theHeap)

        for j in range(k):
            tuplePoints = heapq.heappop(theHeap)
            res.append(points[tuplePoints[1]])
        return res