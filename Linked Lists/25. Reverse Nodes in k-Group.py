# =============================================================
#  Problem: 25. Reverse Nodes in k-Group (https://leetcode.com/problems/reverse-nodes-in-k-group/)
#  Description: Reverse nodes of a linked list in groups of size k.
#  Approach: Recursively reverse k nodes at a time
# =============================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Step 1: Check if there are at least k nodes left in the list
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1

        # If fewer than k nodes, no reversal; return head as-is
        if count < k:
            return head

        # Step 2: Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next  # store next
            curr.next = prev       # reverse current pointer
            prev = curr            # move prev forward
            curr = next_node       # move curr forward

        # Step 3: Recursively process the remaining list
        head.next = self.reverseKGroup(curr, k)

        # Return the new head of the reversed group
        return prev
