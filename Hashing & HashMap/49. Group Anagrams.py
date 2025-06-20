#  Problem Link: https://leetcode.com/problems/group-anagrams/
#  Approach: Use sorted word as a key (anagram signature) in a dictionary
#  Time Complexity: O(n * k log k), where n = number of words and k = max word length


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group words by their anagram signature
        anagram_groups = defaultdict(list)

        for word in strs:
            # Sort the characters in the word to create a signature
            signature = ''.join(sorted(word))

            # Group all words with the same signature
            anagram_groups[signature].append(word)

        # Return all grouped anagram lists
        return list(anagram_groups.values())
