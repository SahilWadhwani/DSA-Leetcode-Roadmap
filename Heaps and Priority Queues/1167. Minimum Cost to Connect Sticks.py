"""
LeetCode: 1167. Minimum Cost to Connect Sticks  
Difficulty: Medium  
Link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/

Approach:
----------
This is a classic **Greedy + Min-Heap** problem.

We repeatedly combine the two smallest sticks until one stick remains:
1. Push all stick lengths into a **min-heap**.
2. While more than one stick remains:
    - Pop the two smallest.
    - Add their lengths (this is the cost of the operation).
    - Push the resulting stick back into the heap.
3. Keep a running total of all operation costs.

This greedy approach ensures we always combine the smallest pairs first, minimizing total cost.

Time Complexity: O(n log n)  
    - Building the heap takes O(n)
    - Each of n-1 operations takes O(log n)

Space Complexity: O(n)
"""


class Solution:

	def minCostToCombineSticks(self, sticks: List[int]) -> int:
		if len(sticks) < 1:
			return 0

		min_heap = []
		final = 0

		for stick in sticks:
			heapq.heappush(min_heap, stick)
		
		while len(min_heap) > 1:
			res = 0
			for i in range(2):
				res += heapq.heappop(min_heap)
			heapq.heappush(min_heap, res)
			final += res
				
		return final
	
