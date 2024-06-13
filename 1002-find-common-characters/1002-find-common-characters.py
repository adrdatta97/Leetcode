class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first = Counter(words[0])
        for i in words:
            cur_cnt = Counter(i)
            for c in first:
                first[c] = min(first[c], cur_cnt[c])
        res = []
        for c in first:
            for i in range(first[c]):
                res.append(c)
        return res
        