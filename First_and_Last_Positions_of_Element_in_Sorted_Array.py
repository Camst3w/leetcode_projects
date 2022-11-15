class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        current_range = [-1, -1]
        try:
            current_range[0] = nums.index(target)
            nums.reverse()
            current_range[1] = len(nums) - 1 - nums.index(target)
            return current_range
        except ValueError:
            return [-1, -1]


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
