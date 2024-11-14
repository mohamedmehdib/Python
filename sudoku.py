class Solution:
    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        num = str(k)
                        if (self.validSquare(board, num, i, j) and 
                            self.validHorizontally(board, num, i) and 
                            self.validVertically(board, num, j)):
                            board[i][j] = num
                            if self.solveSudoku(board):
                                return True
                            board[i][j] = "."
                    return False
        return True

    def validSquare(self, board, num, row, col):
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == num:
                    return False
        return True

    def validHorizontally(self, board, num, row):
        for j in range(9):
            if board[row][j] == num:
                return False
        return True

    def validVertically(self, board, num, col):
        for i in range(9):
            if board[i][col] == num:
                return False
        return True

    def printBoard(self, board):
        for i in range(9):
            for j in range(9):
                if j % 3 == 2:
                    print(board[i][j], end="|")
                else:
                    print(board[i][j], end=" ")
            print()
            if i % 3 == 2:
                print("- " * 9)

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

sol.solveSudoku(board)
sol.printBoard(board)
