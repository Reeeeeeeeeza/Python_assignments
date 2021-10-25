import numpy as np
class queue:
    def __init__(self,size):    #constructor
        self.size=size          
        self.arr=np.array([self.size]) #implementing the numpy array
        self.front=self.rear=-1        #the front and rear of queue must be -1 at initials
    
    def enqueue(self,data):           #takes data to be enqueued as arg.
        if self.isFull():             #calling fun isFull
            print("Queue Overflow!")
        else:
            self.rear+=1    #as values are enqueud from rear so the index is incremented by 1
            if self.front==-1:       #checks if front is -1 change it to 0
                self.front+=1

        self.arr[self.rear]=data     
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow!"
        else:
            val=self.arr[self.front] 
            self.front =self.front+1 
            return val
    def isFull(self):
        return (self.rear == self.size-1) #returns true if cond true else false
    
    def isEmpty(self):
        return ((self.front==-1 or self.rear ==-1))# returns true if cond true else false
q=queue(4)
q.enqueue(1)
print(q.dequeue())
