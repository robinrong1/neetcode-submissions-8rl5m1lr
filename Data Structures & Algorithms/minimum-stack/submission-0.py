class MinStack:

    def __init__(self):
        self.stack = []
        self.mvStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        smaller = min(self.mvStack[-1], val) if self.mvStack else val
        self.mvStack.append(smaller)

    def pop(self) -> None:
        self.stack.pop()
        self.mvStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mvStack[-1]
