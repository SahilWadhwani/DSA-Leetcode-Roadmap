#  Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
#  Approach: Bucket Sort — group elements by frequency and iterate in reverse
#  Time Complexity: O(n), Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build a frequency map
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Create buckets where index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 3: Iterate buckets in reverse to get k most frequent elements
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
