# =============================================================================
#  Problem: 101. Symmetric Tree
#  Link: https://leetcode.com/problems/symmetric-tree/

#  Approach:
#   - Use recursive DFS to compare left and right subtrees.
#   - Two trees are mirrors if:
#       1. Their root values are the same
#       2. left.left is mirror of right.right
#       3. left.right is mirror of right.left
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to check if two trees are mirror images
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
            )

        # Edge case: empty tree is symmetric
        if not root:
            return True
        
        return isMirror(root.left, root.right)
