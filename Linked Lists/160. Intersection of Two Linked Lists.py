#  Problem Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
#  Approach: Length Alignment — bring both pointers to the same starting distance from the end
#  Time Complexity: O(n + m), Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Step 1: Get lengths of both lists
        currA, currB = headA, headB
        lenA = lenB = 0

        while currA:
            lenA += 1
            currA = currA.next

        while currB:
            lenB += 1
            currB = currB.next

        # Step 2: Reset pointers to heads
        currA, currB = headA, headB

        # Step 3: Move the pointer of the longer list forward to align lengths
        while lenA > lenB:
            currA = currA.next
            lenA -= 1

        while lenB > lenA:
            currB = currB.next
            lenB -= 1

        # Step 4: Move both pointers together until they meet
        while currA and currB:
            if currA == currB:
                return currA  # Intersection node found
            currA = currA.next
            currB = currB.next

        return None  # No intersection
