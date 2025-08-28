# =============================================================================
#  Problem: 94. Binary Tree Inorder Traversal
#  Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

#  Description:
#   Given the root of a binary tree, return the inorder traversal of its nodes' values.

#  Inorder Traversal (LNR):
#   - Traverse left subtree
#   - Visit root
#   - Traverse right subtree
#
#  Approaches:
#   1. Recursive (DFS)
#   2. Iterative using stack
#
#  Complexity:
#   - Time: O(n)
#   - Space: O(n) worst case due to recursion stack or manual stack
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # ==============================
        #  Iterative Inorder Traversal
        # ==============================
        res = []
        stack = []
        curr = root

        # Keep traversing left until none is left
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the node
            curr = stack.pop()
            res.append(curr.val)

            # Visit the right subtree
            curr = curr.right

        return res

        # ==============================
        #  Recursive Version (Alternative)
        # ==============================
        # res = []
        # def inorder(node):
        #     if not node:
        #         return
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)

        # inorder(root)
        # return res
