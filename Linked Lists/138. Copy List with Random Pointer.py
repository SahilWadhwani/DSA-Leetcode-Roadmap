#  Problem Link: https://leetcode.com/problems/copy-list-with-random-pointer/
#  Approach: Two-pass HashMap — first pass copies nodes, second links `next` and `random`
#  Time Complexity: O(n), Space: O(n)

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}  # Map from original node → copied node
        curr = head

        #  First pass: Copy all nodes (values only, no links yet)
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        #  Second pass: Set up next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new.get(curr.next)
            if curr.random:
                old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        # Return the new head
        return old_to_new[head]
