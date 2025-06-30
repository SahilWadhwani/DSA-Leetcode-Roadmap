#  Problem Link: https://leetcode.com/problems/ransom-note/
#  Approach: Use frequency maps to compare counts of each character
#  Time Complexity: O(n + m), where n = length of ransomNote, m = length of magazine


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rnDict = defaultdict(int)  # Count of characters in ransomNote
        mgDict = defaultdict(int)  # Count of characters in magazine

        # Count characters needed for the ransom note
        for char in ransomNote:
            rnDict[char] += 1

        # Count available characters from the magazine
        for char in magazine:
            mgDict[char] += 1

        # Check if magazine has enough of each character
        for char in rnDict:
            if mgDict[char] < rnDict[char]:
                return False

        return True
