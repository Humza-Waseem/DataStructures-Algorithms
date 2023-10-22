class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queue = [None] * maxSize
        self.front = -1
        self.back = -1

    def is_empty(self):
        if(self.front == -1 and self.back == -1):
           return True
        else:
            return False

    def is_full(self):
        if((self.back + 1) % self.maxSize == self.front):
                        # it checks if the [(back+1) % maxSize]= front index ,,,then return TRUE
          return True

        else:
            return False

    def enqueue(self, value):
        if (self.is_full() == True):
            return "Queue Already Full"
        elif (self.is_empty() == True):
            self.front = 0
            self.back = 0
        else:
            self.back = (self.back + 1) % self.maxSize
        self.queue[self.back] = value

    def dequeue(self):
        if (self.is_empty() == True):
            return "queue is empty"
        elif (self.front == self.back):
            self.front = -1
            self.back = -1
        else:
            self.front = (self.front + 1) % self.maxSize
        return self.queue[self.front]

    def peek(self):
        if (self.is_empty() == True):
            return "Queue is empty"
        else:
            return self.queue[self.front]   # returning the front elemnt from Queue


queue = Queue(6)   # giving the max size as 6

queue.enqueue(1)    # top
queue.enqueue(2)   # top + 1
queue.enqueue(3)   #top + 2


print(queue.peek())   #  1
queue.dequeue()       #  1 will be removed
print(queue.peek())   #  2
queue.dequeue()       #  2 will be removed
print(queue.peek())   #  3
queue.dequeue()       #  3 will be removed

# print(queue.size())  
