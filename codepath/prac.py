# from collections import deque

# def __init__(self):
#         self.queue = deque()
      
        
        
        
# def ping(self, t: int) -> int:

#         self.queue.append(t)

#         while self.queue and self.queue[0] + 3000 < t:
#             self.queue.popleft()

#         return len(self.queue)
       


# def __init__(self):
#         self.stack = []
#         self.minStack = []
        

# def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        

# def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()
        

# def top(self) -> int:
#         return self.stack[-1]
      
        
# def getMin(self) -> int:
#         return self.minStack[-1]


# convert stack to queue

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:

        return (len(self.s1) or len(self.s2))==0
        
