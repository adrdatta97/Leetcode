class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = {}
        for i in nums:
            n[i] = nums.count(i)
        for key, value in n.items():
            if value == len(nums)//2:
                return key
        