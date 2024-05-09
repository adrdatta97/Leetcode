class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        c = 0

        for num1, num2 in zip(sorted(nums1), sorted(nums2)):
          c = num2 - num1

        return c
        