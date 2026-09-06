class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =set()
        l = 0
        while l < len(nums):
            if nums[l] in seen:
                return True
            else:
                seen.add(nums[l])
                l += 1
        return False