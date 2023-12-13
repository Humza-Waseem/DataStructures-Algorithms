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
            nextNode = current.next  # assigning current.next to nextNode variable so that we don't lose track of the next node when we change the direction of the pointer

            current.next = prev # changing the direction of the pointer

            prev = current  # moving prev one step forward in the list . In the first step the prev will be None, but in the next step it will be the first node of the list , then the second node and so on.....

            current = nextNode # moving current one step forward in the list. In the first step the current will be the first node of the list, then the second node and so on.....

        self.head = prev   # in the end the prev will contain the last node of the list, so we assign the prev to the head of the list. This will make the last node of the list as the first node of the list and the list will be reversed.


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
linked_list.PrintLinkedList(1)
linked_list.reverse()
linked_list.PrintLinkedList(1)

val = linked_list.GetNodeValue(index)

print(f"Node value at Index {index} is {val}")
Target = 4
if linked_list.search(Target):
    print(f"Node with value {Target} FOUND in the linked list.")
else:
    print(f"Node with value {Target} NOT FOUND in the linked list.")
