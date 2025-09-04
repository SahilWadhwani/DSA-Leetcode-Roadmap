# =============================================================================
#  Problem: 102. Binary Tree Level Order Traversal
#  Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

#  Approach:
#   - Use Breadth-First Search (BFS) with a queue.
#   - Track the number of nodes at the current level.
#   - For each level, collect values and enqueue left/right children.
#
# 🧠 Time Complexity: O(n) — visit every node once
# 🧠 Space Complexity: O(w) — width of the binary tree (max queue size)
# =============================================================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []

        queue = deque([root])  # BFS queue
        result = []

        while queue:
            level_size = len(queue)   # Number of nodes at current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Enqueue children of current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add current level to final result
            result.append(current_level)

        return result
