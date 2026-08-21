class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sorts = "" .join(sorted(s))
            hashmap[sorts].append(s)
        return list(hashmap.values())