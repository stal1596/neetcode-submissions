class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs: 
            s += str(len(word)) + "#"+ word
        return s

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            j = 0
            while s[i + j] != '#':
                j += 1
            length = int(s[i: i+j])
            word = s[i+j+1: i+j+1+length]
            res.append(word)
            i = i + j + 1 + length
        return res