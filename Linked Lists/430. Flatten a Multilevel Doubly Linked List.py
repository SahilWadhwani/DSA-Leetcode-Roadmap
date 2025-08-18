#  Problem Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
#  Approach: Splice each child list in-place:
#    - For any node with a child, find the child's tail, connect tail ↔ next,
#      then connect node ↔ child and null the child pointer.
#  Time Complexity: O(n) average, but worst-case can be O(n^2) if many nodes have long children
#     (because we scan to each child's tail every time). A stack-based DFS is O(n).

# Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

from typing import Optional

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            if curr.child:
                # Walk down the child list to find its tail
                child_tail = curr.child
                while child_tail.next:
                    child_tail = child_tail.next

                # Stitch child's tail to curr.next (if it exists)
                if curr.next:
                    child_tail.next = curr.next
                    curr.next.prev = child_tail

                # Splice child list right after curr
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None  # child consumed

            # Move forward
            curr = curr.next

        return head
