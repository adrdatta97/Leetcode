class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        import itertools
        merged = sorted(list(itertools.chain(*grid)))
        lg = len(merged)
        g = []
        m = []
        for i in range(1, lg+1):
            g.append(i)
        for i in merged:
            if merged.count(i) > 1 and i not in m:
                m.append(i)
        for i in g:
            if i in g and i not in merged:
                m.append(i)
        return m