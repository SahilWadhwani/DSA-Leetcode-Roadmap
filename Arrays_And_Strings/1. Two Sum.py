#  Problem Link: https://leetcode.com/problems/two-sum/
#  Approach: Use HashMap to track complements while iterating
#  Time Complexity: O(n)

def twoSum(nums, target):
    # Create a dictionary to store numbers we've seen so far and their indices
    seen = {}

    # Loop through the array with both index and value
    for i, num in enumerate(nums):
        # For each number, calculate what we need to reach the target
        diff = target - num

        # If we've already seen the difference before, we found our answer
        if diff in seen:
            return [seen[diff], i]  # Return the indices of the two numbers

        # Otherwise, store the current number with its index
        seen[num] = i

    # In case there's no solution (though the problem guarantees one)
    return []
