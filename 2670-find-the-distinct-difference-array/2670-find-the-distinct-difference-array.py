class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = []
        prefix = 0
        suffix = 0
        
        for i in range(1, len(nums)+1):
            prefix = len(list(set(nums[:i])))
            suffix = len(list(set(nums[i:])))
            n.append(prefix-suffix)
            prefix = 0
            suffix = 0
            
        return n