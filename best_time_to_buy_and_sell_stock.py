class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if (prices[j] - prices[i]) > max_profit:
        #             max_profit = prices[j] - prices[i]
        # return max_profit

        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(current_profit, max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit


sol = Solution()
print(sol.maxProfit([7, 6, 4, 3, 1]))
