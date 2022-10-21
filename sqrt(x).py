class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0
        while True:
            if (y+1)*(y+1) > x:
                return y
            y += 1


sol = Solution()
print(sol.mySqrt(0))
