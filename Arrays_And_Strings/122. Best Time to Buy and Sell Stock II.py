#  Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#  Approach: Greedy — grab every increasing pair as profit
#  Time Complexity: O(n)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # Start from day 1 and compare each day with the previous one
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        # This strategy simulates buying and selling on every upward trend
        return profit
