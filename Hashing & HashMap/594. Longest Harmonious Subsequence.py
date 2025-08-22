# =============================================================
#  Problem: 594. Longest Harmonious Subsequence (https://leetcode.com/problems/longest-harmonious-subsequence/)
#  Description: Find the length of the longest subsequence where the difference 
#     between the maximum and minimum values is exactly 1.
#  Approach: Count frequency of each number, check pairs (num, num+1) 
#     and track the maximum combined frequency.
# =============================================================


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Count the frequency of each number
        freq = Counter(nums)
        longest = 0

        # For each number, check if num+1 exists to form a harmonious pair
        for num in freq:
            if num + 1 in freq:
                # Update longest with the total frequency of num and num+1
                longest = max(longest, freq[num] + freq[num + 1])

        return longest
