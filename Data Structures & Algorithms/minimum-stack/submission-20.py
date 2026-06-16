class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_values[-1] if self.min_values else val)
        self.min_values.append(val)
        # if val <= self.min:
        #     self.min = val
        #     self.min_values.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        #if val == self.min_values[-1]:
        self.min_values.pop()
        #    self.min = self.min_values[-1] if self.min_values else float('inf')
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
