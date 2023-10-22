class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)

    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False
        
    def pop(self):

        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "stack Empty"
    
    
    def peek(self):
        if  self.isEmpty() != True:
            return self.stack[-1]
        else:
            return "stack is Empty"

    # def size(self):
    #     return len(self.stack)

stack = Stack()
# STACK EMPTY AT FIRST
print(stack.isEmpty())

# PUSHING THE ELEMENTS IN THE STACK
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# POPPING THE ITEMS FROM STACK AS "LAST IN FIRST OUT"
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())

