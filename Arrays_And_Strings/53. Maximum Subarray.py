#  Problem Link: https://leetcode.com/problems/maximum-subarray/
#  Approach: track running sum and reset when it dips below 0
#  Time Complexity: O(n)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Stores the best sum we've seen so far
        current_sum = 0          # Running sum of the current subarray

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            # If the current sum goes negative, start a new subarray
            if current_sum < 0:
                current_sum = 0

        return max_sum
