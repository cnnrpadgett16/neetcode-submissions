class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        rpn_stack = []
        
        ## tokens = ['3', '4', '+', '5', '*']
        ## rpn_stack = [5, 7]
        ## next_operator = 
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '/', '*']:
                rpn_stack.append(int(tokens[i]))
            else:
                operator1 = rpn_stack.pop()
                operator2 = rpn_stack.pop()
                if tokens[i] == '+':
                    next_operator = operator2 + operator1
                elif tokens[i] == '-':
                    next_operator = operator2 - operator1
                elif tokens[i] == '/':
                    next_operator = int(operator2 / operator1)
                else:
                    next_operator = operator2 * operator1
                rpn_stack.append(next_operator)
        return rpn_stack.pop()

        
        