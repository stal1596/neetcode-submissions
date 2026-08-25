class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        a = sorted(hashmap)

        if not a:
            return 0

        count = 1
        longest = 1

        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 1:
                count += 1
            else:
                count = 1

            longest = max(longest, count)

        return longest