#  Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/
#  Approach: Use a set to check sequence starts in O(1) time and count consecutive numbers
#  Time Complexity: O(n), Space: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Convert list to set for O(1) lookups
        longest = 0

        for num in num_set:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                # Count forward while next consecutive number exists
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # Update the maximum length found
                longest = max(longest, length)

        return longest
