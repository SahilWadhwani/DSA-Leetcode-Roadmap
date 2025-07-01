#  Problem Link: https://leetcode.com/problems/word-pattern/
#  Approach: Use two hash maps to maintain a bijection between characters and words
#  Time Complexity: O(n), where n = number of words


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charToWord = {}
        wordToChar = {}

        words = s.split()

        # Early exit if lengths don't match
        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            # If we've seen this character before, check it maps to the same word
            if c in charToWord:
                if charToWord[c] != w:
                    return False

            # If we've seen this word before, check it maps to the same character
            if w in wordToChar:
                if wordToChar[w] != c:
                    return False

            # Save the new mappings
            charToWord[c] = w
            wordToChar[w] = c

        return True
