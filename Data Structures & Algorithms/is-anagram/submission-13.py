class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s, hashmap_t = {} , {}
        if len(s) == len(t):
            for cha_s in s:
                hashmap_s[cha_s] = 1 + hashmap_s.get(cha_s,0)
            for cha_t in t:
                hashmap_t[cha_t] = 1 + hashmap_t.get(cha_t,0)
            if hashmap_t == hashmap_s:
                return True
            else:
                return False
        else:
            return False