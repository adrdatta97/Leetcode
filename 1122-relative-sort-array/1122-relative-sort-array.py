class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = {}
        r = []
        s = []
        for i in arr2:
            ans[i] = arr1.count(i)
        for key,value in ans.items():
            for i in range(value):
                r.append(key)
        for i in arr1:
            if i not in arr2:
                s.append(i)
        rs = sorted(s)
        return r+rs
            
        