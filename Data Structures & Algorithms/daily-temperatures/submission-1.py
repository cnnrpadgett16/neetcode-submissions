class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        my_stack = []
        ## temp = [30, 38, 30, 36, 35, 40, 28]
        ## my_stack = [(30, 0), ()]
        for index, temp in enumerate(temperatures):
            while my_stack and temp > my_stack[-1][0]:
                  stack_temp, stack_index = my_stack.pop()
                  result[stack_index] = index - stack_index
            my_stack.append((temp, index))
        
        return result




        