class MinStack:

    def __init__(self):
        self.normal = []
        self.minstack = []

    def push(self, val: int) -> None:
        minval = self.minstack[-1] if self.minstack else val
        self.normal.append(val)
        self.minstack.append(min(minval, val))
    def pop(self) -> None:
        self.minstack.pop()
        self.normal.pop()

    def top(self) -> int:
        return self.normal[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
