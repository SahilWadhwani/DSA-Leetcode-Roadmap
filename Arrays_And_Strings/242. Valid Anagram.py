#  Problem Link: https://leetcode.com/problems/valid-anagram/
#  Approach: Sort both strings and compare (can also use HashMap/Counter)
#  Time Complexity: O(n log n) due to sorting

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  Quick and simple approach: sort both strings and compare
        return sorted(s) == sorted(t)

        #  Alternative approach using frequency count
        # return Counter(s) == Counter(t)

        #  Manual frequency count using defaultdict
        # if len(s) != len(t):
        #     return False

        # dictS = defaultdict(int)
        # dictT = defaultdict(int)

        # for char in s:
        #     dictS[char] += 1

        # for char in t:
        #     dictT[char] += 1

        # return dictS == dictT
