class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def Enqueue(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def dequeue(self):
        pop=self.head
        self.head=self.head.next
        pop.next=None
        self.length-=1
        return pop.value
    
    def peek(self):
        return self.head.value
    
    def delete(self):
        self.head=None
        self.tail=None
    
    def __str__(self):
        temp=self.head
        result=' '
        while temp is not None:
            result += str(temp.value)
            if temp.next:
                result+='->'
            temp=temp.next
        return result
    
new_linked_list=LinkedList()
new_linked_list.Enqueue(10)
new_linked_list.Enqueue(20)
new_linked_list.Enqueue(30)
print(new_linked_list.peek())
print(new_linked_list.dequeue())
print(new_linked_list)
