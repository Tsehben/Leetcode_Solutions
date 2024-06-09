def __init__(self):
        self.queue = deque()
      
        
        
        

def ping(self, t: int) -> int:

        self.queue.append(t)

        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()

        return len(self.queue)
       