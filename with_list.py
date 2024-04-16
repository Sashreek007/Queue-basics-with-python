
class Queue:
    def __init__(self):
        self.list=[]

    def Enqueue(self,value):
        self.list.append(value)
    
    def __str__(self):
        result=''
        for i in self.list:
            result+=str(i)
            result+=' '
        return result
    
    def Dequeue(self):
        del self.list[0]

    def Peek(self):
        return self.list[0]

custom_queue=Queue()
custom_queue.Enqueue(1)
custom_queue.Enqueue(2)
custom_queue.Enqueue(3)
custom_queue.Dequeue()
print(custom_queue.Peek())
custom_queue.Dequeue()
print(custom_queue)



