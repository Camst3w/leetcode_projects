class Solution:
    def maximumScore(self, nums: list, multipliers: list) -> int:
        score = 0
        while multipliers and nums:
            largest_start, largest_end, mult_s, mult_e = -9999999, -9999999, 0, 0
            for i in multipliers:
                if nums[0] * i >= largest_start:
                    largest_start, mult_s = nums[0] * i, i
                if nums[-1] * i >= largest_end:
                    largest_end, mult_e = nums[-1] * i, i
            if largest_end > largest_start:
                score += largest_end
                multipliers.remove(mult_e)
                nums.pop(-1)
            else:
                score += largest_start
                multipliers.remove(mult_s)
                nums.pop(0)
        return score


sol = Solution()
print(sol.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))

# need dp and tle?