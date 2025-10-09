"""
LeetCode: 150. Evaluate Reverse Polish Notation  
Difficulty: Medium  
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Approach:
---------
We use a stack to evaluate expressions written in Reverse Polish Notation (postfix notation).  
For every token:
- If it's a number, push it to the stack.
- If it's an operator (+, -, *, /), pop two operands from the stack, perform the operation, and push the result back.

Note:
- Integer division should truncate toward zero (as per the problem statement), so we cast the result using `int()` after division.

Time Complexity: O(n) — Each token is processed once.  
Space Complexity: O(n) — Stack grows in proportion to number of tokens.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()

                # Perform operation in correct order: val2 <op> val1
                if token == '+':
                    res = val2 + val1
                elif token == '-':
                    res = val2 - val1 
                elif token == '*':
                    res = val2 * val1 
                elif token == '/':
                    res = int(val2 / val1)  # Truncate toward zero

                stack.append(res)
            else:
                stack.append(int(token))  # Convert number string to int

        return stack[-1]  # Final result is on top of stack
