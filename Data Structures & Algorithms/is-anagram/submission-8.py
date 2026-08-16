class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hashmap1 = {}
            hashmap2 = {}
            for char,lett in zip(s,t):
                if char in hashmap1:
                    hashmap1[char] +=1
                else:
                    hashmap1[char] = 1
                if lett in hashmap2:
                    hashmap2[lett] +=1
                else:
                    hashmap2[lett] = 1
            if hashmap1 == hashmap2:
                return True
            else:
                return False