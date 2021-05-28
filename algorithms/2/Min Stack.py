class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> None:
        self.list.pop()        

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()