#  Problem Link: https://leetcode.com/problems/linked-list-cycle/
#  Approach 1: Hash Set to detect repeated nodes (O(n) space)
#  Approach 2: Floyd’s Cycle Detection Algorithm (fast & slow pointers) — O(1) space
#  Time Complexity: O(n), where n is the number of nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #  Approach 1: Hash Set (O(n) space)
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False

        #  Approach 2: Fast and Slow Pointer (Floyd’s Cycle Detection) — O(1) space
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Pointers met — cycle exists

        return False  # Fast pointer reached end — no cycle
