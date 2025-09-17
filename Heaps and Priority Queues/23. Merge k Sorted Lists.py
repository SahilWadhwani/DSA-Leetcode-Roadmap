# =============================================================================
#  Problem: 23. Merge k Sorted Lists
#  Link: https://leetcode.com/problems/merge-k-sorted-lists/
#
#  Description:
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and optimize the time complexity.
#
# Example:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
#
# Constraints:
# - k == lists.length
# - 0 <= k <= 10^4
# - 0 <= lists[i].length <= 500
# - -10^4 <= lists[i][j] <= 10^4
# - lists[i] is sorted in ascending order.
# =============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Uses a min-heap (priority queue) to efficiently merge k sorted linked lists.

        Time Complexity: O(N log k), where N is the total number of nodes and
                         k is the number of lists.
        Space Complexity: O(k), for the heap storing one node from each list.
        """

        heap = []
        dummy = ListNode(0)
        curr = dummy

        # Step 1: Push the head of each non-empty list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # use (val, index, node) to avoid comparison error

        # Step 2: Pop the smallest node and push its next node to the heap
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
