# =============================================================================
#  Problem: 108. Convert Sorted Array to Binary Search Tree
#  Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

#  Approach:
#   - Use a recursive divide-and-conquer method.
#   - Pick the middle element as the root to maintain balance.
#   - Recursively apply the same logic to the left and right subarrays.
#
#  Time Complexity: O(n) — each element is visited once.
#  Space Complexity: O(log n) — due to recursion stack in a balanced tree.
# =============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Helper function to construct BST recursively
        def convertToBST(nums, left, right):
            if left > right:
                return None  # base case: empty subarray
            
            mid = (left + right) // 2  # choose middle element for balance
            
            root = TreeNode(nums[mid])  # create node with middle value
            
            # Recursively build left and right subtrees
            root.left = convertToBST(nums, left, mid - 1)
            root.right = convertToBST(nums, mid + 1, right)
            
            return root

        # Edge case: empty input
        if not nums:
            return None

        return convertToBST(nums, 0, len(nums) - 1)
