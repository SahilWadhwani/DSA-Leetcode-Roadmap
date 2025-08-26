# =============================================================================
#  Problem: 216. Combination Sum III (https://leetcode.com/problems/combination-sum-iii/)
#  Description:
#   Find all possible combinations of `k` numbers that add up to `n`, 
#   using numbers from 1 to 9, where each number is used at most once.
#
#  Approach:
#   - Use backtracking to explore all combinations starting from 1 to 9.
#   - Add numbers to a path and track the total sum.
#   - If the total equals `n` and the length of the path is `k`, it's a valid combo.
#   - Prune the path if the sum exceeds `n`.
#
#  Complexity:
#   - Time: O(C(9, k)) => bounded because only 9 numbers can be used.
#   - Space: O(k) recursion depth for the path.
# =============================================================================

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int], total: int) -> None:
            # Base case: valid combination
            if total == n and len(path) == k:
                res.append(path.copy())
                return

            # Prune if total exceeds target or path too long
            if total > n or len(path) > k:
                return

            for i in range(start, 10):  # numbers from 1 to 9
                # Early pruning: skip if adding this will exceed the target
                if total + i > n:
                    break

                path.append(i)                          # Choose
                backtrack(i + 1, path, total + i)      # Explore
                path.pop()                             # Undo

        backtrack(1, [], 0)
        return res
