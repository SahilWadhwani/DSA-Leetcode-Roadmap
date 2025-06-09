#  Problem Link: https://leetcode.com/problems/happy-number/
#  Approach: Use a set to detect cycles while repeatedly replacing the number with the sum of squares of its digits
#  Time Complexity: O(log n) per transformation (because digit count is log n), and at most few hundred transformations

class Solution:
    def isHappy(self, n: int) -> bool:

        # Helper to calculate sum of squares of digits of a number
        def happyHelper(n: int) -> int:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        seen = set()  # to detect loops

        # Repeat the process until we reach 1 (happy) or loop (not happy)
        while n != 1:
            if n in seen:
                return False  # we've been here before → it's looping
            seen.add(n)
            n = happyHelper(n)  # replace n with the sum of squares of its digits

        return True  # reached 1 → it's a happy number
