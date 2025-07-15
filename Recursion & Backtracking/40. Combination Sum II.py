#  Problem Link: https://leetcode.com/problems/combination-sum-ii/
#  Approach: Backtracking with sorting + skip duplicates to avoid repeated combinations
#  Time Complexity: O(2^n), with pruning via duplicate checks


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to group duplicates together

        def backtrack(start, path, total):
            # Base Case 1: Exceeded the target
            if total > target:
                return

            # Base Case 2: Found a valid combination
            if total == target:
                res.append(path.copy())
                return

            # Iterate through candidates starting from `start` index
            for i in range(start, len(candidates)):
                #  Skip duplicates on the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose the current element
                path.append(candidates[i])

                # Recurse with i + 1 because each number can only be used once
                backtrack(i + 1, path, total + candidates[i])

                # Backtrack: remove last element
                path.pop()

        backtrack(0, [], 0)
        return res
