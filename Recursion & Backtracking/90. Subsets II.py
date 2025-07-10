#  Problem Link: https://leetcode.com/problems/subsets-ii/
#  Approach: Backtracking + Sorting to skip duplicate subsets
#  Time Complexity: O(2^n), due to subset generation, with pruning via deduplication


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to make duplicate elements adjacent

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return 

            #  Include the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)

            #  Exclude the current element (backtrack)
            subset.pop()

            # Skip all duplicates of the current element
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Move to the next distinct element
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
