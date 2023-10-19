class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None     # returns true if the stack is none

    def push(self, data):
        new_node = Node(data)     # Here, a new instance of the Node class is created. This new node is initialized with the data provided.
        new_node.next = self.top    #This line establishes the link between the new node and the rest of the stack. The next attribute of the new node is set to point to the current top element of the stack. This is because the new node will become the new top, and its next should point to the previous top to maintain the stack structure.
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        else:
            return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()  # Output: 3 -> 2 -> 1 -> None

print("Peek:", stack.peek())  # Output: Peek: 3

print("Pop:", stack.pop())    # Output: Pop: 3

stack.display()  # Output: 2 -> 1 -> None


