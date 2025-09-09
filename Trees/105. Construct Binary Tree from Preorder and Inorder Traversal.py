# =============================================================================
#  Problem: 105. Construct Binary Tree from Preorder and Inorder Traversal
#  Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#  Approach:
# • The first element in preorder is always the root.
# • Use the root to split inorder into left and right subtrees.
# • Recur on the corresponding slices of preorder and inorder arrays.
#
# ⏱ Time Complexity: O(n^2) — due to repeated index lookup in `inorder`.
#  Space Complexity: O(n) — due to recursion stack.
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Base case: when traversal arrays are empty
        if not preorder or not inorder:
            return None

        # First element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of root in inorder traversal
        idx = inorder.index(root_val)

        # Build left and right subtrees recursively
        # Left subtree: preorder[1:1+idx], inorder[:idx]
        # Right subtree: preorder[1+idx:], inorder[idx+1:]
      
        root.left = self.buildTree(preorder[1 : 1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])

        return root
