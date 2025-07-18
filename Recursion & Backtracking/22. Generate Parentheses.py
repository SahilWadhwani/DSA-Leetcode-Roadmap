#  Problem Link: https://leetcode.com/problems/generate-parentheses/
#  Approach: Backtracking — build valid combinations by tracking open and closed counts
#  Time Complexity: O(2^n), but only valid combinations are built → Catalan Number C(n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []       # Final result list
        stack = []     # Current parenthesis string being built

        def backtrack(openCount, closedCount):
            #  Base case: if we've added all valid open and close brackets
            if openCount == closedCount == n:
                res.append("".join(stack))
                return

            # Add an open bracket if we haven't used up all n
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closedCount)
                stack.pop()

            # Add a closing bracket only if it won't break validity
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()

        backtrack(0, 0)
        return res
