#  Problem Link: https://leetcode.com/problems/isomorphic-strings/
#  Approach: Use two hash maps to ensure one-to-one mapping between characters of both strings
#  Time Complexity: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Maps to store the character mapping from s → t and t → s
        map_s_t = {}
        map_t_s = {}

        for char1, char2 in zip(s, t):
            # If mapping exists, it must match the current character
            if char1 in map_s_t and map_s_t[char1] != char2:
                return False
            if char2 in map_t_s and map_t_s[char2] != char1:
                return False

            # Store the new mapping
            map_s_t[char1] = char2
            map_t_s[char2] = char1

        return True
