class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first, second = 2**31, 2**31
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False 



sol = Solution()
print(sol.increasingTriplet([6, 7, 1, 8, 2]))
