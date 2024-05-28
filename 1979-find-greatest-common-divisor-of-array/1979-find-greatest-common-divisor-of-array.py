class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math
        n = sorted(nums)
        N = []
        N.append(n[0])
        N.append(n[-1])
        
        def divisorGen(n):
            large_div = []
            for i in range(1, int(math.sqrt(n)+1)):
                if n % i == 0:
                    yield i
                    if i * i != n:
                        large_div.append(n/i)
            for div in reversed(large_div):
                yield int(div)
        
        first = list(divisorGen(N[0]))
        last = list(divisorGen(N[1]))
        
        for j in reversed(first):
            if j in last:
                return j
                break