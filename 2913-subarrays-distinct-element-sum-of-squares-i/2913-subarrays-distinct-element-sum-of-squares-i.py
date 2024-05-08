class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        lnums = len(nums)
        r = []

        def displaysubarr(nums):
          res = [[]]
          for i in range(lnums + 1):
            for j in range(i+1, lnums+1):
              sub = nums[i : j]
              res.append(sub)
          return res

        subarr = displaysubarr(nums)

        for i in subarr[1:]:
          r.append(len(set(i))**2)
        
        return sum(r)

