#  Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#  Approach: Two-pointer technique with a dummy node to handle edge cases
#  Time Complexity: O(n), Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (like removing head)
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # Move first pointer (n + 1) steps ahead to maintain gap of n
        for _ in range(n + 1):
            first = first.next

        # Move both pointers together until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Now second is right before the node to delete
        second.next = second.next.next

        return dummy.next  # Return the new head
