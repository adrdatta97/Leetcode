class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        x = []

        for i in nums1:
          if i in nums2:
            x.append(i)
        for i in nums2:
          if i in nums3 and i not in x:
            x.append(i)
        for i in nums3:
          if i in nums1 and i not in x:
            x.append(i)
        return list(set(x))
