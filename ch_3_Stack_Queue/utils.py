class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.idx = 0
    
    def push(self, data):
        self.stack[self.idx] = data
        self.idx+=1
    
    def pop(self):
        data = self.stack[self.idx]
        self.idx-=1
        return data
    
    def peek(self):
        return self.stack[self.idx]
    
    def isEmpty(self):
        return self.idx == 0
    
class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.end = 0
        self.start = 0
    
    def push(self, data):
        self.queue[self.end] = data
        self.end += 1
    
    def pop(self):
        data = self.queue[self.start]
        self.start -= 1
        return data
    
    def peak(self):
        return self.queue[self.start]
    
    def isEmpty(self):
        return self.start == 0