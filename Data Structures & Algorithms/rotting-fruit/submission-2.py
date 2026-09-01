class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rotten = set()
        fresh = set()
        ROW, COL = len(grid), len(grid[0])

        def addOrange(r, c):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in rotten or grid[r][c] == 0):
                return
            q.append((r,c))
            rotten.add((r,c))
            fresh.remove((r,c))
        

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i,j))
                    rotten.add((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        minute = -1
        while q:

            for r in range(len(q)):
                r, c = q.popleft()
                addOrange(r,c+1)
                addOrange(r+1,c)
                addOrange(r-1,c)
                addOrange(r,c-1)
            minute += 1
        return -1 if fresh else minute
