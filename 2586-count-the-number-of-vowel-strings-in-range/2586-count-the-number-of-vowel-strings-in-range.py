class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        w = words[left:right+1]
        ans = 0
        v = ['a', 'e', 'i', 'o', 'u']
        for i in w:
            if i[0] in v and i[-1] in v:
                ans += 1
        return ans
                
            
                
        