class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Top 2 most frequent element
        '''
        hashmap = defaultdict(list)
        for num in nums:
            hashmap[num] =  1 + hashmap.get(num,0)
        return sorted(hashmap, key=hashmap.get, reverse=True)[:k]




            