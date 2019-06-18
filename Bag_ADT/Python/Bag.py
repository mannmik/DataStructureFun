
class Bag:

    def __init__(self):
        self.bagContainer = []


    def add(self, val):
        self.bagContainer.append(val)
    

    def contains(self, val):
        
        for i in self.bagContainer:
            if i == val:
                return True
            
        return False

    
    def remove(self, val):
        for i in self.bagContainer:
            if i == val:
                self.bagContainer.remove(i)