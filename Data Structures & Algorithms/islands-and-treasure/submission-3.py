class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        def addRoom(i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 or (i,j) in visited):
                return
            visited.add((i,j))
            q.append((i,j))




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        dist = 0
        while q:
            for r in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r,c+1)
                addRoom(r-1,c)
                addRoom(r,c-1)
            dist += 1