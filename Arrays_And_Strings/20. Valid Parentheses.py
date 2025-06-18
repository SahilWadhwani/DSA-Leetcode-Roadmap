#  Problem Link: https://leetcode.com/problems/valid-parentheses/
#  Approach: Use a stack to match closing brackets with the most recent opening bracket
#  Time Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpen:
                # Check if the top of the stack matches the expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Valid pair, pop the opening bracket
                else:
                    return False  # Mismatch or empty stack — invalid
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(c)

        # If the stack is empty, all brackets matched correctly
        return not stack
