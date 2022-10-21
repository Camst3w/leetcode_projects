class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth = sorted([sum(customer) for customer in accounts], reverse=True)
        return wealth[0]


sol = Solution()
print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))
