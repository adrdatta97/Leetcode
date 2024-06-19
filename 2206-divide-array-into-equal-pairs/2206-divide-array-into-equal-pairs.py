class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = 0 
        num = sorted(nums)
        n = list(zip(num[::2], num[1::2]))
        for i, j in n:
            if i==j:
                c += 1
            if i != j:
                return False
        return True
        