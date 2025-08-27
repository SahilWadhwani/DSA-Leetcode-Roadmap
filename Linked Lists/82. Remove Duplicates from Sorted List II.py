#  Problem: 82. Remove Duplicates from Sorted List II
#  Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#

#  Approach:
#   - Use a dummy node before the head to simplify deletion logic at the head.
#   - Traverse the list using two pointers: `prev` (last confirmed unique node)
#     and `curr` (current node being evaluated).
#   - If a duplicate is found (i.e., curr.val == curr.next.val), skip all duplicates.
#   - Connect `prev.next` to the node after the duplicates.
#   - If not duplicate, simply move `prev` forward.
#
#  Complexity:
#   - Time: O(n), where n is the number of nodes
#   - Space: O(1), in-place list manipulation


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases cleanly (e.g., head is duplicate)
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            is_duplicate = False

            # Skip all nodes that have the same value as curr
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                is_duplicate = True

            if is_duplicate:
                # Skip all duplicates
                prev.next = curr.next
            else:
                # No duplicate, move prev forward
                prev = prev.next

            # Move curr forward in all cases
            curr = curr.next

        return dummy.next
