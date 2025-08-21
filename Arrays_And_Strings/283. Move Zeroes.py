# =============================================================
#  Problem: 283. Move Zeroes (https://leetcode.com/problems/move-zeroes/)
#  Description: Move all zeros to the end of the array while maintaining the order of non-zero elements.
#  Approach: Two-pointer technique — overwrite non-zeros first, then fill the rest with zeros.
# =============================================================

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Pointer to place the next non-zero element
        insert_pos = 0

        # First pass: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Second pass: fill remaining positions with zero
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
