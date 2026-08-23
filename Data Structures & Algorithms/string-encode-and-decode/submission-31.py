class Solution:

    def encode(self, strs: List[str]) -> str:
        s =""
        for char in strs:
            s += str(len(char)) +'#'+ char
        return s 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])

            word = s[j + 1:j + 1 + length]
            strs.append(word)

            i = j + 1 + length

        return strs
