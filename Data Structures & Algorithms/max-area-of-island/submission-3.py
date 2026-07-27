class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        maxArea = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0):
                return 0

            area = 1
            grid[r][c] = 0
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r+1,c)
            area += dfs(r, c-1)
            return area
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea