"""
LeetCode: 239. Sliding Window Maximum  
Difficulty: Hard  
Link: https://leetcode.com/problems/sliding-window-maximum/

Approach:
----------
We use a **monotonic deque** to efficiently track the maximum in each sliding window of size `k`.

Deque stores indices of elements in decreasing order:
1. We remove indices from the back if the current number is greater (they can't be max).
2. We remove the front if it's outside the current window.
3. The max of each window is always at the front of the deque.

Time Complexity: O(n)  
Space Complexity: O(k)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Holds indices of useful elements for current window

        for i in range(len(nums)):
            # Step 1: Remove elements out of window from front
            if q and q[0] < i - k + 1:
                q.popleft()

            # Step 2: Maintain decreasing order of elements in deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Step 3: Add current element index to deque
            q.append(i)

            # Step 4: Append max for this window to result
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
