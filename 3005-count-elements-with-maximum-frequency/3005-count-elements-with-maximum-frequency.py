class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = dict()
        c = 0
        for i in nums:
          count[i] = count.get(i, 0) + 1 
        for k in count.values():
          if k == max(count.values()):
            c += k

        return c