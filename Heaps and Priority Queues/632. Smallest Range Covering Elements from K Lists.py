"""
LeetCode: 632. Smallest Range Covering Elements from K Lists
Difficulty: Hard
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

Approach:
---------
We use a **min-heap** to always track the current minimum value across the k lists,
while maintaining a variable `current_max` to store the maximum value at each step.

Steps:
1. Initialize the heap with the first element of each list.
2. Track the current max value seen across all lists.
3. Continuously pop the smallest value (min of heap), check range with `current_max`.
4. Push the next element from the same list into the heap and update `current_max`.
5. Stop once any list runs out of elements (since range must include one from each).

Time Complexity: O(N log k), where N is the total number of elements and k is the number of lists.
Space Complexity: O(k) for the heap.

Notes:
------
✔ Maintains smallest window [min, max] covering all lists.
✔ Smart use of heap allows moving the pointer only where needed.
"""

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        k = len(nums)
        min_heap = []  # stores (value, list_id, index_in_list)
        current_max = float("-inf")

        # Step 1: Initialize heap with first element from each list
        for i in range(k):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            current_max = max(current_max, val)

        best_range = [float("-inf"), float("inf")]

        # Step 2: Process until one of the lists runs out of elements
        while min_heap:
            min_val, list_id, idx = heapq.heappop(min_heap)

            # Update the best range if smaller or equally sized but more left-aligned
            if (current_max - min_val < best_range[1] - best_range[0]) or 
               (current_max - min_val == best_range[1] - best_range[0] and min_val < best_range[0]):
                best_range = [min_val, current_max]

            # If possible, push the next element from the same list into the heap
            if idx + 1 < len(nums[list_id]):
                next_val = nums[list_id][idx + 1]
                heapq.heappush(min_heap, (next_val, list_id, idx + 1))
                current_max = max(current_max, next_val)
            else:
                break  # One list is exhausted

        return best_range
