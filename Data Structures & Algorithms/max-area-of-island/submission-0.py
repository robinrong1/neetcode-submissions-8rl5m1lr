class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # 1. Base Case: Out of bounds OR water (0)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            # 2. Mark as visited by "sinking" the island (turn 1 to 0)
            grid[r][c] = 0

            # 3. Explore all 4 directions and accumulate area
            # 1 (current cell) + North + South + West + East
            area = 1
            area += dfs(r - 1, c) # Up
            area += dfs(r + 1, c) # Down
            area += dfs(r, c - 1) # Left
            area += dfs(r, c + 1) # Right

            return area

        # Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # Found unvisited land; measure the whole island
                    current_island_area = dfs(r, c)
                    max_area = max(max_area, current_island_area)

        return max_area