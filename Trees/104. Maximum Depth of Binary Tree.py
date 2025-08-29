# =============================================================================
#  Problem: 104. Maximum Depth of Binary Tree
#  Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
#  Description:
#   Given the root of a binary tree, return its maximum depth.
#   A binary tree's maximum depth is the number of nodes along the longest
#   path from the root node down to the farthest leaf node.

#  Approach:
#   - Use recursive DFS (Depth-First Search).
#   - Base case: If node is None, return depth 0.
#   - Recursive case: Return 1 + max depth of left and right subtrees.
#
#  Complexity:
#   - Time: O(n), where n is the number of nodes
#   - Space: O(h), where h is the height of the tree (due to recursion stack)
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the current node is null, return 0
        if not root:
            return 0
        
        # Recursive case: 1 (current node) + max depth of left/right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
