class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # index and height

        
        for i, h in enumerate(heights + [0]): ## sentinel trick to flush all the stack at the end.
            start = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        # for i, h in stack:
        #     max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
        




