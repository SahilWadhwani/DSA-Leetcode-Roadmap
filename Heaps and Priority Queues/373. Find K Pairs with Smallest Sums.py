"""
LeetCode: 373. Find K Pairs with Smallest Sums
Difficulty: Medium
Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

Approach:
---------
 Brute-force (commented out):
    - Generate all pairs (nums1[i], nums2[j])
    - Push their sums into a max-heap of size k
    - Time: O(m * n * log k), where m and n are lengths of nums1 and nums2

 Optimized approach (uses sorted nature of arrays):
    - We treat the problem like a matrix of sums, where:
        - Row = nums1[i]
        - Column = nums2[j]
    - Only explore next smallest pair using a min-heap
    - Start by pairing each nums1[i] with nums2[0] (up to k)
    - At each step, push (nums1[i], nums2[j+1]) to explore next in row
    - Time: O(k log k), Space: O(k)
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        res = []

        # Only go up to k elements in nums1 to keep heap size in check
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            # Each heap entry: (sum, index in nums1, index in nums2)

        while min_heap and len(res) < k:
            total, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            # Move to the next element in nums2 while keeping nums1[i] constant
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
