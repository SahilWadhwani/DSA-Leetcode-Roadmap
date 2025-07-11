#  Problem Link: https://leetcode.com/problems/combination-sum/
#  Approach: Backtracking — explore all combinations with unlimited reuse of elements
#  Time Complexity: O(2^t), where t = target (worst case: each element is 1)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            #  Base case: total exceeded target
            if total > target:
                return

            #  Found a valid combination
            if total == target:
                res.append(path.copy())
                return

            # Try every candidate starting from current index (allows unlimited reuse)
            for i in range(start, len(candidates)):
                path.append(candidates[i])                     # Choose
                backtrack(i, path, total + candidates[i])      # Explore
                path.pop()                                     # Un-choose (backtrack)

        backtrack(0, [], 0)
        return res
