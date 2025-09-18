"""
LeetCode: 215. Kth Largest Element in an Array

Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Approach:
----------
We maintain a **min-heap of size k** to track the k largest elements.
As we iterate over the array, we:
1. Add each element to the heap.
2. If heap size exceeds k, we remove the smallest element.
3. At the end, the smallest element in the heap is the k-th largest overall.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap to store the k largest elements
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # Keep heap size at most k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The top of the heap is the k-th largest
        return min_heap[0]
