#  Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#  Approach: Sliding Window using a Set to track unique characters
#  Time Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To keep track of characters in the current window
        longest = 0       # Result variable
        left = 0          # Left boundary of the sliding window

        for right in range(len(s)):
            # If character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the new character and update max length
            char_set.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
