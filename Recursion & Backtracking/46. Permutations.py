#  Problem Link: https://leetcode.com/problems/permutations/
#  Approach: Backtracking — build all possible arrangements using a "used" tracker
#  Time Complexity: O(n!), where n = len(nums)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            #  Base case: if the path includes all numbers
            if len(path) == len(nums):
                res.append(path.copy())
                return

            # Try every unused number
            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack(path, used)

                # Un-choose (backtrack)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return res
