class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, volume = 0, len(heights)-1, 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            k = width * height
            volume = max(volume, k)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1     
        return volume
        