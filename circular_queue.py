class Queue:
    def __init__(self,maxsize):
        self.items= maxsize*[None]
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
    
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    
    def Enqueue(self,value):
        if self.isFull():
            return "It is full"
        else:
            if self.top+1==self.maxsize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value
        return "Done"
    
    def Dequeue(self):
        first_element=self.items[self.start]
        start=self.start
        if self.start==self.top:
            self.start=-1
            self.top=-1
        elif self.start==self.maxsize:
            self.start=0
        else:
            self.start+=1
        self.items[start]=None
        return first_element
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items= self.maxsize*[None]
        self.start=-1
        self.top=-1
        
custom_queue=Queue(3)
print(custom_queue.isFull())
print(custom_queue.isEmpty())
custom_queue.Enqueue(2)
custom_queue.Enqueue(3)
custom_queue.Enqueue(4)
print(custom_queue.peek())
print(custom_queue.Dequeue())
print(custom_queue)
custom_queue.delete()
print(custom_queue)
    