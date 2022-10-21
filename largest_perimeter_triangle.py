class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)

        while sorted_nums[-3] + sorted_nums[-2] <= sorted_nums[-1]:
            sorted_nums.pop()
            if len(sorted_nums) < 3:
                return 0

        return sum(sorted_nums[-3:])


sol = Solution()
print(sol.largestPerimeter([1, 2, 1]))
