class Solution:
    def search(self, x, y, matrix):

        for i in range(y):
            if matrix[i][x] == "Q":
                return False
        

        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if matrix[j][i] == "Q":
                return False
            i -= 1
            j -= 1
        

        i, j = x + 1, y - 1
        while i < len(matrix) and j >= 0:
            if matrix[j][i] == "Q":
                return False
            i += 1
            j -= 1
        
        return True

    def solveNQueens(self, n):
        results = []
        if 1 <= n <= 9:
            matrix = [["."] * n for _ in range(n)]
            self.placeQueens(matrix, 0, n, results)
        return [["".join(row) for row in result] for result in results]

    def placeQueens(self, matrix, row, n, results):
        if row == n:
            results.append([row.copy() for row in matrix])
            return
        
        for col in range(n):
            if self.search(col, row, matrix):
                matrix[row][col] = "Q"
                self.placeQueens(matrix, row + 1, n, results)
                matrix[row][col] = "."

sol = Solution()
result = sol.solveNQueens(4)
print(result)
