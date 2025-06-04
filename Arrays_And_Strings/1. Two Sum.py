class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in present:
                return [present[complement], i]
            present[num] = i

        return []
