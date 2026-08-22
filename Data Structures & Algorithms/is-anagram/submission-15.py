class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)
        if len(s) != len(t):
            return False
        else:
            for char in s:
                hashmap_s[char] += 1
            for char in t:
                hashmap_t[char] += 1   
            if hashmap_t == hashmap_s:
                return True
            else:
                return False
