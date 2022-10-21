class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == len(nums2) == 0:
            return 0
        nums = sorted(nums1 + nums2)
        print(nums)
        if len(nums) % 2 > 0:
            return float(nums[(len(nums) - 1)//2])
        else:
            return float((nums[(len(nums))//2 - 1] + nums[(len(nums))//2]) / 2)


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [4, 2]))
