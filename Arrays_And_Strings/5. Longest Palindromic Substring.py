#  Problem Link: https://leetcode.com/problems/longest-palindromic-substring/
#  Approach: Expand around each character (and between characters) to find longest palindrome
#  Time Complexity: O(n^2), Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Base case: empty or single character string is already a palindrome
        if len(s) < 2:
            return s

        longest = ""

        # Helper function to expand around a center and return the longest palindrome found
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # slice from the last matched pair
            return s[left + 1: right]

        # Try every character as a center
        for i in range(len(s)):
            # Odd-length palindrome (center at i)
            odd = expand_around_center(i, i)
            if len(odd) > len(longest):
                longest = odd

            # Even-length palindrome (center between i and i+1)
            even = expand_around_center(i, i + 1)
            if len(even) > len(longest):
                longest = even

        return longest
