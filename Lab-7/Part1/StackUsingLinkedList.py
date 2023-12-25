class Node:
    def __init__(self, data):
        self.data = data
        self.next = None          # Next is a Pointer that points to the next node in the stack

class Stack:
    def __init__(self):
        self.top = None    # Top is a Pointer that points to the top of the stack


    def isEmpty(self):      # returns true if the stack is none
        if(self.top is None):
           return True   
        else:
            return False

    def push(self, data):
        newNode = Node(data)     # Here, a new instance of the Node class is created. This new node is initialized with the data provided.
        newNode.next = self.top   # Set the next pointer of the new node to point to the current top of the stack(the top of stack which was before pushing newNode ). This makes the new node the top of the stack.

        self.top = newNode   # new node will now become Top of the stack

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            val = self.top.data   # to get the data of the top node

            self.top = self.top.next  # Now the top will be pointing to next element.After popping, self.top.next will become top
            return val


    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:

            return self.top.data


    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


stack = Stack()

stack.push(1)

stack.push(2)

stack.push(3)


stack.display()  

print("Peek Value  : ",stack.peek())  

print("Pop:", stack.pop())   


stack.display() 


