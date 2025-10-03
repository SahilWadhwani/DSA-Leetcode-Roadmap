"""
LeetCode: 20. Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Approach:
---------
We use a stack to keep track of opening brackets.
For every closing bracket encountered, we check if it matches the last opening bracket on the stack.

1. If it matches, we pop the opening bracket.
2. If it doesn't match or the stack is empty when we encounter a closing bracket, the string is invalid.
3. After processing all characters, if the stack is empty, the string is valid.

Time Complexity: O(n) - We process each character once.
Space Complexity: O(n) - In the worst case, we store all characters in the stack.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            # If it's a closing bracket, check if it matches the top of the stack
            if bracket in close_to_open:
                if stack and stack[-1] == close_to_open[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(bracket)

        # If stack is empty, all brackets matched
        return not stack
