class Solution:
    def sortSentence(self, s: str) -> str:
        S = s.split(' ')
        l = {}
        sv = ""
        for i in S:
          key = ''.join(filter(str.isdigit, i))
          val = ''.join(filter(str.isalpha, i))
          l[int(float((key)))] = val
        sl = sorted(l)
        for i in sl:
          sv += l[i]
          sv += ' '
        return sv.rstrip()
            
        