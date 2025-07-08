#  Problem Link: https://leetcode.com/problems/count-nice-pairs-in-an-array/
#  Approach: Use HashMap with key = num - rev(num); count pairs based on frequency
#  Time Complexity: O(n), Space: O(n)


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        count = 0 
        MOD = 10**9 + 7

        # Helper to reverse digits of a number
        def rev(n):
            return int(str(n)[::-1])

        for num in nums:
            # The difference between num and its reverse defines its "nice pair class"
            key = num - rev(num)

            # If this key has been seen before, all those occurrences form a nice pair with this one
            count = (count + freq[key]) % MOD

            # Update frequency for this key
            freq[key] += 1

        return count
