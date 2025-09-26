"""
LeetCode: 621. Task Scheduler  
Difficulty: Medium  
Link: https://leetcode.com/problems/task-scheduler/

Approach:
----------
We solve this problem using a **Greedy strategy with a Max-Heap** and a **cooldown queue**.

Goal: Schedule tasks such that the same task is separated by at least `n` units of time.

Steps:
1. Use a **max heap** to always pick the task with the highest frequency.
   - Store negative frequencies to simulate a max heap using Python's min heap.
2. Use a **cooldown queue** (`deque`) to keep track of tasks waiting to be re-executed.
   - Each task in cooldown is stored as a tuple: `(time_task_can_be_reexecuted, remaining_count)`
3. In each time unit:
   - Try to run the most frequent task available (from heap).
   - If it’s not finished (frequency > 0), push it into cooldown with updated time.
   - If a task’s cooldown expires (i.e., it's valid to run again), push it back to heap.

Early exit optimization:
- Skip idle time as soon as all tasks are finished and cooldown is empty.

Time Complexity: O(n log n)  
Space Complexity: O(n)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Max-heap using negative frequencies
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # stores tuples of (ready_time, -count)

        while max_heap or cooldown:
            time += 1

            # Step 1: Execute task from heap if available
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # reduce count (note: it's negative)

                # If more of this task remains, push to cooldown with cooldown expiry time
                if count != 0:
                    cooldown.append((time + n, count))

            # Step 2: Reactivate any task whose cooldown has expired
            if cooldown and cooldown[0][0] == time:
                _, ready_task = cooldown.popleft()
                heapq.heappush(max_heap, ready_task)

        return time
