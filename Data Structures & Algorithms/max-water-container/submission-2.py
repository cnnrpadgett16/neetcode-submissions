class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        left, right = 0, len(heights) - 1
        # keep track of max area
        max_area = 0

        while left < right:
            ## calculate our current_area
            width = right - left
            height = min(heights[left], heights[right])
            curr_area = width * height

            ## update max_area if curr_area is greater
            max_area = max(curr_area, max_area)

            ## check if left wall is greater than right wall
            ## if it is then move the right pointer to try to find a taller right wall
            if heights[left] > heights[right]:  
                right -= 1
            else: ## move the left pointer to try to find a taller left wall
                left += 1
        
        return max_area
        