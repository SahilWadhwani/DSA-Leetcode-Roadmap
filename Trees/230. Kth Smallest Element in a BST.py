# =============================================================================
#  Problem: 230. Kth Smallest Element in a BST
#  Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#
#  Description:
# Given the root of a binary search tree (BST), and an integer k, return
# the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# Example:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Perform an in-order traversal of the BST,
        which gives the nodes in ascending order.
        Stop the traversal as soon as we reach the kth element.
        """
        self.count = 0     # Counter to keep track of visited nodes
        self.result = 0    # Stores the kth smallest value

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            inorder(node.left)

            # Visit the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return  # Early return, no need to continue traversal

            inorder(node.right)

        inorder(root)
        return self.result
