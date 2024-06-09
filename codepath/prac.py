def __init__(self):
        self.queue = deque()
      
        
        
        
def ping(self, t: int) -> int:

        self.queue.append(t)

        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()

        return len(self.queue)
       


    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
      
        

    def getMin(self) -> int:
        return self.minStack[-1]