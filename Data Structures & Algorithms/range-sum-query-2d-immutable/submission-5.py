class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            prefix = 0
            for col in range(cols):
                prefix += matrix[row][col]
                above = self.prefix_matrix[row - 1][col] if row > 0 else 0
                self.prefix_matrix[row][col] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total = self.prefix_matrix[row2][col2]
        above = self.prefix_matrix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix_matrix[row2][col1 - 1] if col1 > 0 else 0
        top_left = self.prefix_matrix[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0

        return total - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)