class MinStack:

    def __init__(self):
        self.list = []
        self.len = 0
        self.current_min = []

    def push(self, val: int) -> None:
        if self.len == 0:
            self.current_min.append(val)
        self.list.append(val)
        self.len +=1
        if self.current_min[-1]>=val:
            self.current_min.append(val)

    def pop(self) -> None:
        if self.len!=0:
            if self.current_min[-1]==self.list.pop():
                self.current_min.pop()
            self.len-=1

    def top(self) -> int:
        if self.len!=0:
            return self.list[self.len-1]

    def getMin(self) -> int:
        if self.len!=0 and self.current_min: 
            return self.current_min[-1]
