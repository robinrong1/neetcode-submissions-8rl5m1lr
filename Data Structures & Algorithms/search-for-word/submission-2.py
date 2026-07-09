class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if min(row, col) < 0 or row >= len(board) or col >= len(board[0]) or word[i] != board[row][col] or (row, col) in visited:
                return False
            visited.add((row,col))
            res = (dfs(row + 1, col, i + 1) or 
                    dfs(row -1, col, i + 1) or 
                    dfs(row, col + 1, i + 1)or 
                    dfs(row, col - 1, i + 1))

            visited.remove((row,col))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False