class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        m = set()
        for a, b in nums:
            for i in range(a, b+1):
                m.add(i)
            
        return len(m)
        