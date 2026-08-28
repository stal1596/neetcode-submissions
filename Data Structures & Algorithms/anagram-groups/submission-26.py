class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            sorts = ''.join(sorted(word))
            hashmap[sorts].append(word)
        return list(hashmap.values())