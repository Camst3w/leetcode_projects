class Solution:
    def maxArea(self, height: list[int]) -> int:
        current_max = 0
        l_point = 0
        r_point = len(height) - 1
        while l_point < r_point:
            water_vol = (r_point - l_point) * \
                min(height[l_point], height[r_point])
            if water_vol > current_max:
                current_max = water_vol
            if height[l_point] > height[r_point]:
                r_point += 1
            else:
                l_point += 1
        return current_max


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
