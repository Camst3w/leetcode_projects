from math import factorial


class Solution:
    def climbStairs(self, n: int) -> int:
        permutations, j = 0, 0
        if n > 0:
            steps = [1 for i in range(n)]
            permutations += 1
        else:
            return 0
        while steps.count(1) > 1:
            steps.pop()
            steps[j] = 2
            twos, ones = steps.count(2), steps.count(1)
            permutations += int(factorial(len(steps)) /
                                (factorial(twos)*factorial(ones)))
            j += 1
        return permutations


sol = Solution()
print(sol.climbStairs(4))
