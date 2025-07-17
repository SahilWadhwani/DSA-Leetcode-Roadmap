#  Problem Link: https://leetcode.com/problems/word-search/
#  Approach: Backtracking — explore all possible DFS paths from each cell
#  Time Complexity: O(m * n * 4^L), where L = length of the word

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        path = set()  # To keep track of visited cells in the current path

        def backtrack(r, c, i):
            #  If we've matched the entire word
            if i == len(word):
                return True

            #  If out of bounds, already used, or character mismatch
            if (r < 0 or c < 0 or
                r >= rows or c >= columns or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # Mark current cell as visited
            path.add((r, c))

            # Explore all 4 directions (right, down, left, up)
            res = (backtrack(r, c + 1, i + 1) or
                   backtrack(r + 1, c, i + 1) or
                   backtrack(r, c - 1, i + 1) or
                   backtrack(r - 1, c, i + 1))

            # Backtrack — unmark current cell
            path.remove((r, c))
            return res

        # Try every cell as a starting point
        for r in range(rows):
            for c in range(columns):
                if backtrack(r, c, 0):
                    return True

        return False
