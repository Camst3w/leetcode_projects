class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
        # one extra diagonal per layer iterate first layer then add a diagonal list per layer. append and check for same numbers!!


sol = Solution()
print(sol.isToeplitzMatrix([[1, 2], [2, 2]]))
