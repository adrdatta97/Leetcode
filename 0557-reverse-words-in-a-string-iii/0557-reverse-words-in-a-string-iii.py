class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split(' ')
        output = ""
        for i in S:
            output += i[::-1]
            output += " "
        return output.rstrip()
        