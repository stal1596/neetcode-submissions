class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorts = sorted(nums)
        a = set()
        count, longest = 1,0
        for i in range(len(nums)):
            if sorts[i] - 1 in a and sorts[i] != sorts[i-1]:
                count += 1
            if sorts[i] - 1 not in a:
                count = 1
            longest = max(count,longest)
            a.add(sorts[i])
        return longest