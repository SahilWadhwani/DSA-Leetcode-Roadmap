"""
LeetCode: 295. Find Median from Data Stream
Difficulty: Hard
Link: https://leetcode.com/problems/find-median-from-data-stream/

Approach:
----------
We maintain two heaps:
1. A **max-heap (small)** to store the smaller half of the numbers.
2. A **min-heap (large)** to store the larger half of the numbers.

Steps:
- We first push the number into the max-heap (invert sign since Python only has a min-heap).
- We then balance the heaps such that:
    - All elements in `small` are ≤ all elements in `large`.
    - The size difference between heaps is at most 1.
- Median is:
    - The root of the bigger heap if odd count.
    - The average of the roots of both heaps if even count.

Time Complexity:
- addNum(): O(log n)
- findMedian(): O(1)

Space Complexity: O(n)
"""


class MedianFinder:
    def __init__(self):
        # Max-heap (store as negative values)
        self.small = []

        # Min-heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap (inverted)
        heapq.heappush(self.small, -num)

        # Step 2: Ensure ordering between small and large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
