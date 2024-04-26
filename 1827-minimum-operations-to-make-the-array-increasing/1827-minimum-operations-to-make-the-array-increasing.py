class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        l = len(nums)
        for i in range(1, l):
            if nums[i] <= nums[i-1]:
                x= nums[i]
                nums[i] += (nums[i-1]-nums[i]) + 1
                c += nums[i] - x
        return c
        