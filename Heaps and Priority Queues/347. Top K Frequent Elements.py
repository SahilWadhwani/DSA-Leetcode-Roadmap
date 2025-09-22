"""
LeetCode: 347. Top K Frequent Elements  
Difficulty: Medium  
Link: https://leetcode.com/problems/top-k-frequent-elements/

Approach:
----------
We use a **min-heap of size k** to maintain the top k frequent elements.

Steps:
1. Count the frequency of each number using a hashmap (Counter or defaultdict).
2. Push each (frequency, number) pair into a min-heap.
3. Maintain the heap size to k by popping the smallest frequency element.
4. The heap will contain the k most frequent elements.

This solution is more efficient when k is small compared to n.

Time Complexity: O(n log k)  
Space Complexity: O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency count
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Min-heap of size k
        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))

            # Keep the heap size at most k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Extract elements from the heap
        return [num for freq, num in min_heap]
