class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str_digits = ""
        for i in digits:
            str_digits += str(i)
        str_digits = str(int(str_digits) + 1)
        return [int(i) for i in str_digits]


sol = Solution()
print(sol.plusOne([9]))
