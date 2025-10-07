"""
LeetCode: 232. Implement Queue using Stacks  
Difficulty: Easy  
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Approach:
---------
We use **two stacks** to simulate a queue:

1. `input_stack` — handles incoming elements (push operations).
2. `output_stack` — handles outgoing elements (pop/peek operations).

Key Logic:
- On `pop()` or `peek()`, if `output_stack` is empty, we transfer all elements from `input_stack` to `output_stack`. This reverses the order, maintaining FIFO behavior.
- `empty()` returns True only if both stacks are empty.

Time Complexity:
- Amortized O(1) for all operations.
- Worst-case O(n) during transfer, but each element is moved at most once.

Space Complexity: O(n) to store all elements in two stacks.
"""

class MyQueue:

    def __init__(self):
        self.input_stack = []   # Stack for enqueue
        self.output_stack = []  # Stack for dequeue

    def push(self, x: int) -> None:
        # Always push to input stack
        self.input_stack.append(x)

    def pop(self) -> int:
        # Transfer if output stack is empty
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack.pop()

    def peek(self) -> int:
        # Transfer if output stack is empty
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.input_stack and not self.output_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
