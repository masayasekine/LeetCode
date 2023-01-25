from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        while i < len(nums):
            if i != 0 and nums[i] == nums[i-1]:
                del nums[i-1]
                i -= 1
            else:
                cnt += 1
            i += 1
        return cnt

if __name__ == "__main__":
    Solution().removeDuplicates([1,1,2])

