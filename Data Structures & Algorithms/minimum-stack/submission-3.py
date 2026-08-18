class MinStack:
    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minValue: 
            if val > self.minValue[-1]:
                self.minValue.append(self.minValue[-1])
            else:
                self.minValue.append(val)
        else:
            self.minValue.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minValue.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue[-1]