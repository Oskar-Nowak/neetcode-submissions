class MinStack:

    def __init__(self):
        self.stack: list = []
        self._min_stack: list = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self._min_stack.append(val)
        else:
            current_min = min(self._min_stack[-1], val)
            self.stack.append(val)
            self._min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
