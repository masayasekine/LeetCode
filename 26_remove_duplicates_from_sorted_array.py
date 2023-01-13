class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        for i, num in enumerate(nums):
            if num == nums[i-1]:
                del nums[i-1]
            else:
                cnt += 1
        print(nums)
        return cnt

