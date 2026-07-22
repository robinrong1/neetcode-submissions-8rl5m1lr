class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        islands = 0
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                spot = grid[i][j] 
                if spot == "1":
                    bfs(i, j)
                    islands += 1
        return islands
