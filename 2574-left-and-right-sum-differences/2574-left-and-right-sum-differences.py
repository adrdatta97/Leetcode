class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = 0
        left_add = [0]
        f = []
        for i in range(len(nums)):
          l += nums[i]
          if len(left_add) <= len(nums)-1:
            left_add.append(l)
            
        r = 0
        right_add = [0]
        for i in range(len(nums)):
          r += nums[::-1][i]
          if len(right_add) <= len(nums)-1:
            right_add.append(r)
            
        for item in range(len(nums)):
            f.append(abs(left_add[item] - right_add[::-1][item]))
        return f

        