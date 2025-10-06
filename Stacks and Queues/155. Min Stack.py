"""
LeetCode: 155. Min Stack  
Difficulty: Medium  
Link: https://leetcode.com/problems/min-stack/

Approach:
---------
We use two stacks:

1. `main_stack`: Stores all the values pushed by the user.
2. `min_stack`: Tracks the minimum element at every point in time.

- While pushing: 
  - We push the value onto `main_stack`.  
  - If the `min_stack` is empty or the new value is smaller than or equal to the current minimum, we also push it onto `min_stack`.

- While popping:  
  - If the popped value is equal to the top of `min_stack`, we pop it from `min_stack` too (to maintain sync).

- `getMin()`: Returns the top of `min_stack` (the current minimum).
- `top()`: Returns the top of `main_stack`.

Time Complexity: O(1) for all operations  
Space Complexity: O(n) for storing values in both stacks
"""

class MinStack:

    def __init__(self):
        self.main_stack = []  # Stores all values
        self.min_stack = []   # Tracks minimums

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        # Push to min_stack if it's empty or new val is smaller/equal
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.main_stack.pop()

        # If popped value is current min, pop from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
