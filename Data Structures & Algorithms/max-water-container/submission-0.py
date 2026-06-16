class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = -1 
        while left < right:
            width = right - left 
            print(f"Width: {width}")
            if heights[left] < heights[right]:
                area = heights[left] * width
                print(f"Area when left is smaller: {area}")
                left += 1 
            else:
                area = heights[right] * width
                print(f"Area when right is smaller: {area}")
                right -= 1
            
            max_area = max(max_area, area)
        return max_area
        
        


        