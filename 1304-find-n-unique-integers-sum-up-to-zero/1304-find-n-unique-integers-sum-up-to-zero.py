class Solution:
    def sumZero(self, n: int) -> List[int]:
        m = []
        for i in range(1, n//2 +1):
            m.append(i)
            m.append(-i)
        if n % 2 != 0:
            m.append(0)
        return m
        