"""
LeetCode: 739. Daily Temperatures  
Difficulty: Medium  
Link: https://leetcode.com/problems/daily-temperatures/

Approach:
---------
We use a **monotonic decreasing stack** to keep track of indices of previous days whose temperatures are yet to find a warmer future day.

For each temperature:
1. We compare it with the top of the stack.
2. If it is **warmer** than the temperature at the top index of the stack:
   - We pop from the stack and calculate the number of days between the two.
   - Store that difference in the `answer` array.
3. Push the current index onto the stack.

This ensures:
- Every temperature is processed once.
- We only store unresolved temperatures in the stack.

Time Complexity: O(n) — Each index is pushed and popped at most once.  
Space Complexity: O(n) — Stack and answer array.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n             # Initialize result with all zeros
        stack = []                   # Stack to hold indices of unresolved temperatures

        for i, temp in enumerate(temperatures):
            # Check if current temp is warmer than the one at the top of the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day   # Calculate wait time
            stack.append(i)  # Push current day onto the stack

        return answer
