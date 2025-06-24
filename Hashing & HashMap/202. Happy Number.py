#  Problem Link: https://leetcode.com/problems/happy-number/
#  Approach: Use a set to detect cycles while transforming number into sum of squares of digits
#  Time Complexity: O(log n) per transformation, total operations bounded → considered O(1)

class Solution:
    def isHappy(self, n: int) -> bool:

        # Helper function to return sum of squares of digits
        def happyHelper(n: int) -> int:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        seen = set()  # to keep track of previously seen numbers (to detect cycles)

        # Keep computing the sum until we reach 1 (happy) or fall into a cycle
        while n != 1:
            if n in seen:
                return False  # loop detected → not a happy number
            seen.add(n)
            n = happyHelper(n)

        return True  # if we reach 1, it is a happy number
