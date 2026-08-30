class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set:
                    return False
                if board[i][j] !='.':
                    row_set.add(board[i][j])
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] in col_set:
                    return False
                if board[j][i] !='.':
                    col_set.add(board[j][i])
        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    r = square // 3 * 3 + i
                    c = square % 3 * 3 + j
                    if board[r][c] in square_set:
                        return False
                    if board[r][c] !='.':
                        square_set.add(board[r][c])

        return True

