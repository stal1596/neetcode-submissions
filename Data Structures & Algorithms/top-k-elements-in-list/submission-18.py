class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        return sorted(hashmap, key=hashmap.get, reverse=True)[:k]
