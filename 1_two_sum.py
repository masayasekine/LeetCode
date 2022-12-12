from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_a in enumerate(nums):
            for j, num_b in enumerate(nums):
                if i == j:
                    continue
                if num_a + num_b == target:
                    return [i, j]
        return []
