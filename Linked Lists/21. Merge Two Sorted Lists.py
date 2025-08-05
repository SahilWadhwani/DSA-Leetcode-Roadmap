#  Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
#  Approach: Iterative merge using a dummy node
#  Time Complexity: O(n + m), where n and m are the lengths of list1 and list2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify head handling
        dummy = ListNode(-1)
        tail = dummy

        # Traverse both lists and append the smaller node each time
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # One of the lists might still have remaining nodes
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        # Return the merged list starting from dummy.next
        return dummy.next
