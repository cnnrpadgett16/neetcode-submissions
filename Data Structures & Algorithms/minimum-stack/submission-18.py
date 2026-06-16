class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.min = val
            self.min_values.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_values[-1]:
            self.min_values.pop()
            self.min = self.min_values[-1] if self.min_values else float('inf')
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
