class MinStack:

    def __init__(self):
        self.stack=[]
        self.min = 9999999

    def push(self, val: int) -> None:
        if(not self.stack):
            self.stack.append(val)
            self.min = val
        else:
            if self.min>val:
                self.stack.append(2*val-self.min)
                self.min = val
            else:
                self.stack.append(val)
        

    def pop(self) -> None:
        n = self.stack.pop()
        if (self.min>n):
            self.min = 2*self.min - n


    def top(self) -> int:
        if self.min>self.stack[-1]:
            return self.min
        else:
            return self.stack[-1]


    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()