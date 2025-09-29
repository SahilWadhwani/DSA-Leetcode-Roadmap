"""
LeetCode: 973. K Closest Points to Origin
Difficulty: Medium
Link: https://leetcode.com/problems/k-closest-points-to-origin/

Approach:
----------
Use a **max heap** to keep track of the k closest points to the origin (0,0).
1. Calculate the Euclidean distance for each point and push it as negative into a max heap.
2. Keep popping when heap exceeds size `k` so that we are only left with the k closest ones.
3. Finally, return the coordinates from the heap.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        x1, y1 = 0, 0
        max_heap = []
        res = []
        
        def calc(x2: int, y2: int) -> float:
            # Simple Euclidean distance from origin
            res1 = (x1 - x2) ** 2
            res2 = (y1 - y2) ** 2
            return math.sqrt(res1 + res2)

        # iterate through points and maintain max heap of size k
        for x, y in points:
            dist = calc(x, y)
            heapq.heappush(max_heap, (-dist, [x, y]))  # push negative for max-heap behavior

            if len(max_heap) > k:
                heapq.heappop(max_heap)  # remove farthest point

        # extract the k closest points
        for _, pair in max_heap:
            res.append(pair)

        return res 
