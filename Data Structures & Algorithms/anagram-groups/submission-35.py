class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sorts = ''.join(sorted(word))
            res[sorts].append(word)
        return list(res.values())