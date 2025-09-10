# =============================================================================
#  Problem: 116. Populating Next Right Pointers in Each Node
#  Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
#  Description:
# Given a perfect binary tree, populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
#  Note:
# • A perfect binary tree is a type of binary tree in which every parent has two children
#   and all leaf nodes are at the same level.
# • You must use constant extra space. Recursive approach is allowed (stack space doesn't count).
#
# =============================================================================

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # ---------------------------------------------------------------------
        #  BFS Approach (Level-order traversal using queue)
        # • Uses O(N) space for queue — NOT constant space.
        # • Good for understanding how to link next pointers level by level.
        # ---------------------------------------------------------------------
        # if not root:
        #     return None

        # queue = deque([root])

        # while queue:
        #     level_size = len(queue)
        #     for i in range(level_size):
        #         node = queue.popleft()

        #         # Connect current node to the next node in the level
        #         if i < level_size - 1:
        #             node.next = queue[0]

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return root

        # ---------------------------------------------------------------------
        #  Optimized Recursive Approach (Constant Space)
        # • Works because it's a perfect binary tree.
        # • For each node:
        #   - Connect left → right
        #   - Connect right → left of next node (if exists)
        # ---------------------------------------------------------------------
        if not root or not root.left:
            return root

        # Step 1: Link left child → right child
        root.left.next = root.right

        # Step 2: Link right child → left child of root's next (cross-node link)
        if root.next:
            root.right.next = root.next.left

        # Recurse for left and right subtree
        self.connect(root.left)
        self.connect(root.right)

        return root
