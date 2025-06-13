#  Problem Link: https://leetcode.com/problems/merge-intervals/
#  Approach: Sort intervals and merge overlapping ones as we iterate
#  Time Complexity: O(n log n) due to sorting


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # First, sort the intervals based on start time
        intervals.sort()
        merged = []

        for interval in intervals:
            # If merged is empty or there's no overlap, just add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There's an overlap — merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
