class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        m = []
        for i in range(1, len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                m.append(i)                
        return m
        