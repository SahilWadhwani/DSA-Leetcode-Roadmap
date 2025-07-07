#  Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/
#  Approach: Prefix Sum + HashMap to count subarrays with target sum in O(n)
#  Time Complexity: O(n), Space: O(n)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0  # Cumulative sum so far
        count = 0      # Number of subarrays that sum up to k
        prefixMap = defaultdict(int)
        prefixMap[0] = 1  # Base case: a sum of exactly k starting from index 0

        for num in nums:
            prefixSum += num

            # Check if there is a prefix that we can subtract to get sum k
            if (prefixSum - k) in prefixMap:
                count += prefixMap[prefixSum - k]

            # Store/update the frequency of current prefix sum
            prefixMap[prefixSum] += 1

        return count
