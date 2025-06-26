#  Problem Link: https://leetcode.com/problems/contains-duplicate/
#  Approach: Use a set to track seen numbers as we iterate
#  Time Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # Go through each number in the list
        for num in nums:
            if num in seen:
                return True  # Found a duplicate
            seen.add(num)  # Mark this number as seen

        # If we make it here, no duplicates were found
        return False
