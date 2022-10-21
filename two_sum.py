
class Solution:
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            if target - nums[index] in nums and index != nums.index(target - nums[index]):
                return [index, nums.index(target - nums[index])]
        

two_sum = Solution()
print(two_sum.twoSum([2, 7, 11, 15], 9))