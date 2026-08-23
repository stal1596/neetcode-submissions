class Solution:

    def encode(self, strs: List[str]) -> str:
        s =""
        for char in strs:
            s += str(len(char)) +'#'+ char
        return s            

    def decode(self, s: str) -> List[str]:
        strs = list()
        i=0
        while i < len(s): 
            j = i
            length = ''
            while s[j] != '#':
                length += s[j]
                j += 1
            a = int(''.join(length))
            k = j + 1
            wor = list()
            for x in range(a):
                wor.append(s[k+x])
            word = ''.join(wor)
            strs.append(word)
            i = 1+j+a
        return strs

            
                

