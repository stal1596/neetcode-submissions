class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + '#' + word 
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i< len(s):
            length = ""
            while s[i] != '#':
                length += (s[i])
                i += 1
            length = int(length)
            i += 1

            j = 0
            word = ""
            while j < length :
                word += s[i + j]
                j += 1
            i += length
            strs.append(word)
        return strs

