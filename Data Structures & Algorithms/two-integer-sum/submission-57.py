class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        for key, value in enumerate(nums):
            diff = target - value
            if diff in hashmap and hashmap[diff]!=key:
                return [key, hashmap[diff]]