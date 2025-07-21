#  Problem Link: https://leetcode.com/problems/n-queens/
#  Approach: Backtracking with pruning using column and diagonal sets
#  Time Complexity: O(n!), Space: O(n^2) for the board


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to track columns and diagonals where queens already exist
        cols = set()
        posDiag = set()  # (row + col)
        negDiag = set()  # (row - col)

        res = []
        board = [["."] * n for _ in range(n)]  # Initialize empty board

        def backtrack(r):
            # Base case: all rows are filled
            if r == n:
                # Convert board rows to strings and add to result
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                # If the current column or diagonal is attacked, skip
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue 

                # Place queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to next row
                backtrack(r + 1)

                # Backtrack — remove queen and cleanup
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
