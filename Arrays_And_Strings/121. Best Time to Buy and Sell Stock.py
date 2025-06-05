#  Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  Approach: Track the minimum price so far and update max profit on the go
#  Time Complexity: O(n)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start with the highest possible min price (we'll look for the lowest one)
        minPrice = float('inf')
        
        # Initialize profit to 0 — no transactions yet
        maxProfit = 0

        # Go through each price one by one
        for _, price in enumerate(prices):
            # If this price is lower than anything we've seen, update minPrice
            if price < minPrice:
                minPrice = price
            
            # Calculate the profit if we were to sell at this price
            profit = price - minPrice

            # If this is the best profit so far, update it
            if profit > maxProfit:
                maxProfit = profit
            
        return maxProfit
