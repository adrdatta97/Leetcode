class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w = ""
        for i in range(len(word)):
          if ch in word[i]:
            w += word[:i]
            w += word[i]
            break
        w1=word.replace(w,w[::-1]) 
        return w1
        