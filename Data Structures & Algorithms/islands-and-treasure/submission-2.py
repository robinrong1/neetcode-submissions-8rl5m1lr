class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])

        q = deque()
        distance = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                        q.append((i,j))
        directions = [[-1,0], [1,0],[0,1], [0,-1]]
        while q:
            
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    rr = r + dr
                    cc = c + dc
                    if (rr < 0 or cc < 0 or rr >= len(grid) or cc >= len(grid[0]) or grid[rr][cc] != 2147483647):
                        continue
                    grid[rr][cc] = distance
                    q.append((rr,cc))
                
            distance += 1