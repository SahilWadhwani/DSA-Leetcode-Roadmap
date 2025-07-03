#  Problem Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
#  Approach: Use a frequency map to track occurrences of elements from nums1,
# then scan nums2 and collect matches while updating counts
#  Time Complexity: O(n + m), where n = len(nums1), m = len(nums2)


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_count = defaultdict(int)
        result = []

        # Count frequency of each number in nums1
        for num in nums1:
            freq_count[num] += 1

        # For each number in nums2, if it's in the map and count > 0, it's a valid intersection
        for num in nums2:
            if freq_count[num] > 0:
                result.append(num)
                freq_count[num] -= 1  # Use up one occurrence

        return result
