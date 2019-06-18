
class Stack:

    def __init__(self):
        self.stackContainer = []
    

    def push(self, val):
        self.stackContainer.append(val)
    

    def pop(self):
        if not self.isEmpty():
            self.stackContainer.pop()
        
    
    def top(self):
        if not self.isEmpty():
            return self.stackContainer[len(self.stackContainer) - 1]

    def isEmpty(self):
        if len(self.stackContainer) == 0:
            return True
        
        return False

    def size(self):
        return self.stackContainer.count()