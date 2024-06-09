class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = []
        for i in nums:
            if -i in nums:
                n.append(i)
            else:
                n.append(-1)
        return max(n)
        