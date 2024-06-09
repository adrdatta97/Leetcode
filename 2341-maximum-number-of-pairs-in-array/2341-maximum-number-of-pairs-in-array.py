class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = {}
        c,d = 0,0
        res = []
        for i in nums:
            n[i] = nums.count(i)
        for key, value in n.items():
            c += value//2
        for key, value in n.items():
            if value % 2 == 1:
                d += 1
        res.append(c)
        res.append(d)
        return res
        
            
            
            
        
        