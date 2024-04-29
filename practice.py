class Queue:
    def __init__(self,maxsize):
        self.items= maxsize * [None]
        self.maxsize=maxsize
        self.start=-1
        self.top=-1
    
    def __str__(self):
        values =(str(x) for x in self.items) 
        return ' '.join(values)
    
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.top+1==self.maxsize and self.start==0:
            return True   
        else:
            return False