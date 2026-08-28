class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        return sorted(hashmap,key = hashmap.get, reverse = True)[:k]
