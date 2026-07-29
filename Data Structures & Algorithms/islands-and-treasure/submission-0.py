class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        distance = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:

                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or 
                        grid[row][col] != 2147483647):
                        continue
                    
                    grid[row][col] = distance
                    queue.append((row,col))
            distance += 1