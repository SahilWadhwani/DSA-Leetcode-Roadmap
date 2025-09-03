# =============================================================================
#  Problem: 112. Path Sum
#  Link: https://leetcode.com/problems/path-sum/

#  Approach:
#   - Base case: If current node is None, return False
#   - If the current node is a leaf, check if the value matches remaining sum
#   - Recursively check left and right subtrees with updated target
#
#  Time Complexity: O(n), where n is the number of nodes in the tree
#  Space Complexity: O(h), where h is the height of the tree (recursion stack)
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # Base case: empty tree
        if not root:
            return False

        # If it's a leaf node, check if the remaining sum matches
        if not root.left and not root.right:
            return targetSum == root.val

        # Recur for left and right subtrees with reduced target
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )
