class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)
        i = 1
        for num in numbers:
            diff = target - num
            if diff in hashmap:
                return  [hashmap[diff][0],i]
            hashmap[num].append(i)
            i += 1
            