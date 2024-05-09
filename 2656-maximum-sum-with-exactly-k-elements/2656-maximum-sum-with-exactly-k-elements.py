class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        numss = sorted(nums)
        n = numss[-1]
        c = 0
        for i in range(k):
          c += n+i
        return c