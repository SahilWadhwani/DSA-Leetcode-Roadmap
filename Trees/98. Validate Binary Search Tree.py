# =============================================================================
#  Problem: 98. Validate Binary Search Tree
#  Link: https://leetcode.com/problems/validate-binary-search-tree/
#
# 💡 Description:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#   - The left subtree of a node contains only nodes with keys less than the node's key.
#   - The right subtree of a node contains only nodes with keys greater than the node's key.
#   - Both the left and right subtrees must also be binary search trees.
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Uses DFS with range limits (low, high) to validate that all nodes in the tree
        follow the BST property.
        """

        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # An empty node is always valid
            if not node:
                return True

            # Node's value must lie strictly between the allowed range
            if not (low < node.val < high):
                return False

            # Recursively validate left and right subtrees with updated bounds
            return (
                validate(node.left, low, node.val) and
                validate(node.right, node.val, high)
            )

        return validate(root, float('-inf'), float('inf'))
