#  Problem Link: https://leetcode.com/problems/product-of-array-except-self/
#  Approach: Prefix and suffix products to avoid using division
#  Time Complexity: O(n), Space: O(1) extra (excluding output array)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # Initialize result array with 1s

        #  Naive approach (O(n^2), not used)
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if j != i:
        #             product *= nums[j]
        #     res[i] = product
        # return res

        #  Prefix pass — build running product from the left
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        #  Suffix pass — multiply with running product from the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
