# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def traverse(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next

# # Example usage:
# linked_list = LinkedList()
# linked_list.append('a')
# linked_list.append(1)
# linked_list.append('+')

# linked_list.traverse()





################   SEARCH IN A LINKED LIST   #####################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if  self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next != None:
            last = last.next
        last.next = new_node
        
        
       

    def search(self, target):

        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            else:
                current_node = current_node.next
        return False

    def PrintLinkedList(self,target):
        current = self.head
        while current:
            print("{0} -> ".format(current.data), end="")
            current = current.next
        print("None")

    def GetNodeValue(self,index):
        if(index == 0):
            return self.head.data

        
        count = 0
        current = self.head
        while(current != None):
            if(count == index):
                return current.data
            else:
              count = count + 1
              current= current.next
        return None

    def reverse(self):
        

        prev = None
        current = self.head
        while(current):
            nextNode = current.next
            current.next = prev
            prev = current 
            current = nextNode
        self.head = prev


    # def MergeSortedList(self,):



# Example usage:
linked_list = LinkedList()
linked_list2 = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list2.append(1)
linked_list2.append(3)
linked_list2.append(6)
linked_list2.append(8)




index = 3
linked_list.reverse()

val = linked_list.GetNodeValue(index)

print(f"Node value at Index {index} is {val}")
Target = 4
linked_list.PrintLinkedList(1)
if linked_list.search(Target):
    print(f"Node with value {Target} found in the linked list.")
else:
    print(f"Node with value {Target} not found in the linked list.")
