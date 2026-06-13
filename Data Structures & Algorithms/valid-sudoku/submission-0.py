class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # check row and col seperately
            col = [0] * 10
            row = [0] * 10

            # quadrant loc
            sec = [0] * 10
            x = (i % 3) * 3
            y = (i // 3) * 3

            for j in range(9):
                # check row
                if board[i][j] != ".": 
                    num = int(board[i][j])
                    if row[num] >= 1:
                        return False
                    row[int(num)] = 1

                # check col
                if board[j][i] != ".": 
                    num = int(board[j][i])
                    if col[num] >= 1:
                        return False
                    col[int(num)] = 1
                
                # check sec
                if board[x + (j % 3)][y + (j // 3)] != ".":
                    num = int(board[x + (j % 3)][y + (j // 3)])
                    if sec[num] >= 1:
                        return False
                    sec[int(num)] = 1

        
        
        return True
                




