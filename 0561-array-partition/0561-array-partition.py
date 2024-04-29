class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        s = 0
        for i in range(0,len(nums),2):
            s += s_nums[i]
        return s
            
        