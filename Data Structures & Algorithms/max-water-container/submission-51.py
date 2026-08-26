class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_area = max((j-i) * min(heights[i], heights[j]),max_area)
        return max_area
        '''
        max_area,left,right = 0, 0, len(heights)-1
        while left < right:
            max_area = max((right - left) * min(heights[left], heights[right]),max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        

