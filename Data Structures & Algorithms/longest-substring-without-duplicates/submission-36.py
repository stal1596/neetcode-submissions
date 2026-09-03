class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left,r , length = 0, 0, 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            r += 1
            length = max(len(seen),length)

        return length
        