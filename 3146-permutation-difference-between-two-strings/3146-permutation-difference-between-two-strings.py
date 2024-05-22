class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a = 0
        for i in range(len(s)):
            if s[i] in t:
                a += abs(i - t.index(s[i]))
        return a
        