class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = "-" + str(x)[:0:-1]
        else:
            x = str(x)[::-1]
        x = int(x)
        if -2**(31) <= x <= 2**(31) - 1:
            return x
        return 0


sol = Solution()
print(sol.reverse(-120))
