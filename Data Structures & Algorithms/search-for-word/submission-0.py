class Solution:
    directions = ((1,0), (-1,0), (0,1), (0, -1))

    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, visited, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            
            if (i, j) in visited:
                return False
            
            if board[i][j] != word[0]:
                return False
            
            if len(word) == 1:
                return True
            
            visited.add((i, j))
            
            for x, y in self.directions:
                is_valid = dfs(board, word[1:], visited.copy(), i + x, j + y)

                if is_valid:
                    return True
            
            return False
        
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                is_valid = dfs(board, word, set(), i, j)

                if is_valid:
                    return True
            
        return False
        