class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
     def __init__(self):
         self.head = None

     def append(self, data):
        new_node = Node(data)
     

        if self.head is None:   #if the list is empty, add first node at head
             self.head = new_node

             new_node.next = self.head # because it is a circular LL we put the next pointer of the just added node to Point back to the Head
             
        else:  # if the list is not empty, we append the new node at the end of the list

          last = self.head 
          # to check where the node should be placed,, we iterate and try to find the node at which the  "Next" Pointer of "last" points to the "Head"
          while last.next != self.head:
             last = last.next

        #  Once we find the last node, we set its next pointer to point to the new node. This will  append the new node to the end of the list.
          last.next = new_node
        # Finally, we set the next pointer of the new node to point back to the head of the list, making it a circularLinked List
        new_node.next = self.head

     def traverse(self):
          current = self.head
          while current.next != self.head:
            print(current.data)
            current = current.next
          print(current.data)

          # while True:
          #      print(current.data)
          #      current = current.next
          #      if(current == self.head):
          #           break


 

            
  
link = LinkedList()
link.append(5)
link.append(6)
link.append(8)
link.append(10)
link.append(20)

print(link.traverse())


