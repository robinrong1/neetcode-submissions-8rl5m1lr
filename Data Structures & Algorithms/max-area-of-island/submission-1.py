class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        maxArea = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0):
                return 0
            #ITS A 1
            grid[r][c] = 0
            area = 1
            area += dfs(r+1,c)
            area += dfs(r, c+1)
            area += dfs(r-1, c)
            area += dfs(r, c-1)


#u + me = <3
            return area


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    curArea = dfs(r,c)
                    maxArea = max(maxArea, curArea)
        return maxArea
