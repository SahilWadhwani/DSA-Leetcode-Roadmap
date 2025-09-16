# =============================================================================
#  Problem: 236. Lowest Common Ancestor of a Binary Tree
#  Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
#  Description:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes `p` and `q`.
# The lowest common ancestor is defined as the lowest node in the tree that has both `p` and `q`
# as descendants (a node can be a descendant of itself).
#
# Example:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Perform a post-order DFS to find the lowest node that appears
        in the path to both `p` and `q`. If the current node is either `p` or `q`,
        return it. If both left and right subtrees return non-null, this node is the LCA.
        """
        # Base case: if current node is None or matches p or q, return it
        if not root or root == p or root == q:
            return root

        # Recur into left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, current node is the LCA
        if left and right:
            return root

        # Otherwise return non-null result (either left or right)
        return left if left else right
