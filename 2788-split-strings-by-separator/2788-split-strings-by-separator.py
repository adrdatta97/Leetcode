class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for i in words:
            ans += i.split(separator)
        while("" in ans):
            ans.remove("")
        return ans
        