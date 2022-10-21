class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        triangle = [[1], [1, 1]]
        while len(triangle) < numRows:
            next_row = [1]
            for i in range(len(triangle[-1]) - 1):
                next_row.append(triangle[-1][i] + triangle[-1][i+1])
            next_row.append(1)
            triangle.append(next_row)
        return triangle


sol = Solution()
print(sol.generate(5))
