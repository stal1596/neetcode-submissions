class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {value:index for index, value in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]