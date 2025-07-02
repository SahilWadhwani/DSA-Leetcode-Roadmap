#  Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/
#  Approach: Use sets to efficiently find unique common elements
#  Time Complexity: O(n + m), where n = len(nums1), m = len(nums2)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert nums1 to a set for O(1) lookups
        nums1S = set(nums1)
        res = set()

        # Check each number in nums2 — if it's in nums1 set, add to result
        for num in nums2:
            if num in nums1S:
                res.add(num)

        # Convert set to list before returning
        return list(res)
