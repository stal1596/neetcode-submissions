class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for s in strs:
            srtd = ''.join(sorted(s))
            dictionary[srtd].append(s)
        return list(dictionary.values())

        


        