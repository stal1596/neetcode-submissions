class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        # Fill max_left array
        current_max = 0
        for i in range(n):
            max_left[i] = current_max
            current_max = max(current_max, height[i])
            
        # Fill max_right array
        current_max = 0
        for i in range(n - 1, -1, -1):
            max_right[i] = current_max
            current_max = max(current_max, height[i])
            
        # Calculate total trapped water
        total_water = 0
        for i in range(n):
            water_at_i = min(max_left[i], max_right[i]) - height[i]
            if water_at_i > 0:
                total_water += water_at_i
                
        return total_water