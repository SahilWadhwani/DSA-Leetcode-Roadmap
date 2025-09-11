# =============================================================================
#  Problem: 103. Binary Tree Zigzag Level Order Traversal
#  Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
#  Description:
# Given the root of a binary tree, return the zigzag level order traversal
# of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
#
# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True  # Flag to control zigzag direction

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the level list if it's right-to-left
            if not left_to_right:
                current_level.reverse()

            result.append(current_level)
            left_to_right = not left_to_right  # Flip the flag for next level

        return result
