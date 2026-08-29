class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            # Extract length of the word
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            
            length = int(length)
            i += 1  # Skip the '#' delimiter
            
            # Extract the word based on length
            word = ""
            j = 0
            while j < length:
                word += s[i + j]
                j += 1
            
            strs.append(word)
            i += length  # Move pointer past the extracted word
            
        return strs