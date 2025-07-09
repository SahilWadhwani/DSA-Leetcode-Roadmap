#  Problem Link: https://leetcode.com/problems/subsets/
#  Approach: Backtracking — explore all include/exclude decisions for each element
#  Time Complexity: O(2^n), Space: O(n) for recursion stack


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i): 
            # Base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())  # Add the current subset to result
                return 

            # Decision 1: Include the current element
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision 2: Exclude the current element
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
