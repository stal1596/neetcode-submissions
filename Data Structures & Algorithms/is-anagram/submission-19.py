class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                hashmap_s[s[i]] += 1
                hashmap_t[t[i]] += 1   
            if hashmap_t == hashmap_s:
                return True
            else:
                return False
