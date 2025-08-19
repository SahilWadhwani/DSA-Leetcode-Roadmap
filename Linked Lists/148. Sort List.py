# =============================================================
# Problem: 148. Sort List (https://leetcode.com/problems/sort-list/)
# Description: Sort a singly-linked list in O(n log n) time and constant space.
# Approach: Recursive Merge Sort on Linked List
# =============================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: 0 or 1 node is already sorted
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves using slow/fast pointers
        slow, fast = head, head.next  # start fast ahead to find mid before slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'mid' will be the start of the second half
        mid = slow.next
        slow.next = None  # break the list into two halves

        # Step 2: Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Use a dummy node to build the result list
        dummy = ListNode()
        tail = dummy

        # While both lists have nodes, pick the smaller one each time
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # At least one of l1 or l2 is now null
        # Append the remaining non-empty list (if any)
        tail.next = l1 or l2

        # Return the sorted merged list, skipping the dummy node
        return dummy.next
