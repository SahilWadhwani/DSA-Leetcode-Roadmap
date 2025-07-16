#  Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#  Approach: Backtracking — for each digit, explore all possible character mappings
#  Time Complexity: O(4^n), where n is the length of the input digits


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        digits_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                res.append("".join(path))
                return

            # Explore all letter options for the current digit
            possible_letters = digits_to_letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)             # Choose
                backtrack(index + 1, path)      # Explore
                path.pop()                      # Un-choose (backtrack)

        backtrack(0, [])
        return res
