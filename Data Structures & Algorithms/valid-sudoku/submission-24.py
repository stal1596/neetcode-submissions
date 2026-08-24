class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            hashrow = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hashrow:
                    return False
                hashrow.add(board[i][j])
        
        for i in range(9):
            hashcol = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in hashcol:
                    return False
                hashcol.add(board[j][i])
        
        for square in range(9):
            hashsq = set()
            for i in range(3):
                for j in range(3):
                    r = square//3 * 3 + i
                    c = square % 3 * 3 + j
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in hashsq:
                        return False
                    hashsq.add(board[r][c]) 
        return True

                

                
                

                
                