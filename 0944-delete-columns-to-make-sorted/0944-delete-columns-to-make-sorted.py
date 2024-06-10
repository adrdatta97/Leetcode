class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s = 0
        for i in zip(*strs):
            if sorted(i) != list(i):
                s += 1
        return s