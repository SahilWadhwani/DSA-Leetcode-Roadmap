"""
LeetCode: 767. Reorganize String  
Difficulty: Medium  
Link: https://leetcode.com/problems/reorganize-string/

Approach:
----------
We use a **max heap** to always place the character with the highest remaining frequency,
while ensuring that no two adjacent characters are the same.

Steps:
1. Build a frequency map of characters.
2. Push all characters into a max heap based on frequency.
3. Pop the most frequent character, append it to the result.
4. Use a "cooldown" mechanism: hold the previously used character until the next iteration
   to avoid placing the same character adjacently.
5. If after processing, the result length is not equal to the input length, return "" 
   (impossible to reorganize).

Time Complexity: O(n log a)  
    - n = length of string  
    - a = number of unique characters  
Space Complexity: O(n)
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Frequency map
        freq_map = Counter(s)

        # Step 2: Build max heap (store as negative for max-heap behavior)
        max_heap = [(-count, char) for char, count in freq_map.items()]
        heapq.heapify(max_heap)

        res = []
        prev_char, prev_count = "", 0

        # Step 3: Process heap
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)

            # Step 4: Push back previous char if it still has remaining count
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            # Step 5: Update previous char (decrement freq)
            prev_count = count + 1  # since count is negative, adding 1 reduces frequency
            prev_char = char

        result_str = ''.join(res)

        # Step 6: Validate result
        return result_str if len(result_str) == len(s) else ""
