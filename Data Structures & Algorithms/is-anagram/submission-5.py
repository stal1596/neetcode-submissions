class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasmap = {}
        hatmap = {}
        if(len(s)!=len(t)):
            return False
        else:
            for chars in s:
                hasmap[chars] = hasmap.get(chars, 0) + 1
            for chars in t:
                hatmap[chars] = hatmap.get(chars, 0) + 1
            if(hasmap == hatmap):
                return True
            else:
                return False