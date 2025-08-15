#  Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/
# 🧠 Approach 1: Brute Force — Collect all values, sort, and rebuild the list
#  Approach 2 (Recommended): Min Heap (Optimal) — Always pick the smallest node using a priority queue
#  Time Complexity: 
#   - Brute Force: O(N log N)
#   - Min Heap: O(N log k), where N = total nodes, k = number of lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ###  Brute Force Approach — Simple but not optimal
        values = []

        # Collect all node values
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        # Sort the values
        values.sort()

        # Build the new sorted linked list
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next


        ###  Optimal Approach (Min Heap) — Uncomment to use this instead
        # heap = []
        # dummy = ListNode(0)
        # curr = dummy

        # # Step 1: Push head of each list into the heap
        # for i, node in enumerate(lists):
        #     if node:
        #         heappush(heap, (node.val, i, node))  # (value, list_index, node)

        # # Step 2: Process heap
        # while heap:
        #     val, i, node = heappop(heap)
        #     curr.next = node
        #     curr = curr.next

        #     # If there's a next node in the same list, push it into the heap
        #     if node.next:
        #         heappush(heap, (node.next.val, i, node.next))

        # return dummy.next
