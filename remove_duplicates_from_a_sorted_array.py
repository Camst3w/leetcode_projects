class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        previous, i = nums[0], 1
        while i != len(nums):
            if nums[i] != previous:
                previous = nums[i]
                i += 1
            else:
                nums.remove(nums[i])
        return len(nums)


class Solution:  # This is better
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))  # shallow copy
        return len(nums)
# a shallow copy perfroms a copy of the origional list but keeps the same id references.


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
