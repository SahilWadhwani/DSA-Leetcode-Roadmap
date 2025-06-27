#  Problem Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
#  Approach: Sliding Window with Frequency Maps to compare character counts
#  Time Complexity: O(n), where n = length of string s


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        # If p is longer than s, no anagrams possible
        if len(p) > len(s):
            return res

        # Frequency maps for p and the current window in s
        p_count = defaultdict(int)
        window_count = defaultdict(int)

        # Initialize both maps with the first window
        for char in p:
            p_count[char] += 1
        for char in s[:len(p)]:
            window_count[char] += 1

        # Check if the first window is an anagram
        if window_count == p_count:
            res.append(0)

        # Slide the window through s
        for i in range(len(p), len(s)):
            left_char = s[i - len(p)]
            right_char = s[i]

            # Remove the character that's sliding out of the window
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Add the new character entering the window
            window_count[right_char] += 1

            # If current window matches target count, it's an anagram
            if window_count == p_count:
                res.append(i - len(p) + 1)

        return res
