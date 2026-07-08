class MinStack:

    def __init__(self):
        self.list = []
        self.len = 0

    def push(self, val: int) -> None:
        self.list.append(val)
        self.len +=1

    def pop(self) -> None:
        if self.len!=0:
            self.list.pop()
            self.len-=1

    def top(self) -> int:
        if self.len!=0:
            return self.list[self.len-1]

    def getMin(self) -> int:
        if self.len!=0:
            return min(self.list)
        
