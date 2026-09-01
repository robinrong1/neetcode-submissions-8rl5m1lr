class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()

        ROW, COL = len(board), len(board[0])

        for r in range(ROW):
            if board[r][0] == "O":
                q.append((r,0))
            if board[r][COL-1] == "O":
                q.append((r, COL-1))
        for c in range(COL):
            if board[0][c] == "O":
                q.append((0,c))
            if board[ROW-1][c] == "O":
                q.append((ROW-1,c))
        
        while q:
            r,c = q.popleft()
            if r >= 0 and c >= 0 and r < ROW and c < COL and board[r][c] == "O":
                board[r][c] = "A"
                q.append((r,c+1))
                q.append((r+1,c))
                q.append((r,c-1))
                q.append((r-1,c))
            
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "A":
                    board[r][c] = "O"
        