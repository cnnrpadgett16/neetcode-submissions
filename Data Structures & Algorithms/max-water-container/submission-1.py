class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = -1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(area, max_area)
            if heights[right] > heights[left]:
                left+=1
            else:
                right-=1
        return max_area