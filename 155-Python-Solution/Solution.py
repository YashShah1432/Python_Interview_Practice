class MinStack:

    def __init__(self):
        self.st = []
        self.min_stack = []

    def push(self, value: int) -> None:
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        self.st.append(value)
        
        return self.st

    def pop(self) -> None:
        if self.st[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.st.pop()
        return self.st

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()