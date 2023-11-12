import time
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:    # if the BST is Empty   i.e self.root is None
            new_node = Node(value)
            self.root = new_node    # if Tree is empty, create a Node with given value that will be the root node
        else:
            self.insertRecursive(self.root, value)

    def insertRecursive(self, node, value):
        if value < node.value:     # If value is less than the value of the current node value 

            if node.left is None:  # If the left child of the current node is None, it means we've found the appropriate spot for the new node, so we create a new Node with the specified value and set it as the left child of the current node.
                new_node = Node(value)
                node.left = new_node
            else:
                self.insertRecursive(node.left, value)  # if the left child of the current node is not None, we will call the function again and now we will give it the left node as an argument 


        elif value > node.value:  # if value to be inserted is greater than the current node value 
            if node.right is None:
                node.right = Node(value)
            else:
                self.insertRecursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return node.value
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    def inOrderTraversal(self):
        if(self.root is None):
            return None
        else:
            self.inOrderTraversal_recursive(self.root)
        print( "Root Value : ",self.root.value)

    def inOrderTraversal_recursive(self, node):
        if node != None:
            self.inOrderTraversal_recursive(node.left)
            print(node.value, end=" ")
            self.inOrderTraversal_recursive(node.right)
            # print(node.value, end=" ")

# Example usage
bst = BST()
Start = time.time()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(50)
bst.insert(150)
bst.insert(30)
bst.insert(70)
bst.insert(100)
bst.insert(500)
bst.insert(1500)
bst.insert(300)
bst.insert(700)
bst.insert(50)
bst.insert(15000)
bst.insert(30)
bst.insert(7000)
bst.insert(10000)
bst.insert(5000)
bst.insert(15000)
bst.insert(3000)
bst.insert(7000)

bst.inOrderTraversal()
end = time.time()


print(bst.search(7))  # Output: True)
print(bst.search(8))  # Output: False
print(bst.search(20))  
print(bst.search(700))  
print(bst.search(8))  # Output: False
print(bst.search(20))  
print(bst.search(700))  
Total = end - Start
print("Total time to search : ",Total)










# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insertNode(self, x):
#         if not self.root:
#             self.root = Node(x)
#             return self.root

#         current = self.root
#         while current:
#             parent = current
#             if x < current.data:
#                 current = current.left
#             elif x > current.data:
#                 current = current.right
#             else:
#                 return current

#         new_node = Node(x)
#         if x < parent.data:
#             parent.left = new_node
#         else:
#             parent.right = new_node

#         new_node.parent = parent
#         return new_node

#     def findNode(self, x):
#         current = self.root
#         while current:
#             if x < current.data:
#                 if current.left:
#                     current = current.left
#                 else:
#                     return current
#             elif x > current.data:
#                 if current.right:
#                     current = current.right
#                 else:
#                     return current
#             else:
#                 return current

#     def deleteNode(self, x):
#         node = self.findNode(x)
#         if node.data != x:
#             return False

#         def transplant(u, v):
#             if not u.parent:
#                 self.root = v
#             elif u == u.parent.left:
#                 u.parent.left = v
#             else:
#                 u.parent.right = v
#             if v:
#                 v.parent = u.parent

#         if not node.left:
#             transplant(node, node.right)
#         elif not node.right:
#             transplant(node, node.left)
#         else:
#             successor = self.minimum(node.right)
#             if successor.parent != node:
#                 transplant(successor, successor.right)
#                 successor.right = node.right
#                 successor.right.parent = successor
#             transplant(node, successor)
#             successor.left = node.left
#             successor.left.parent = successor

#         return True

#     def inOrderTraversal(self, node):
#         if node:
#             self.inOrderTraversal(node.left)
#             print(node.data, end=" ")
#             self.inOrderTraversal(node.right)

#     def preOrderTraversal(self, node):
#         if node:
#             print(node.data, end=" ")
#             self.preOrderTraversal(node.left)
#             self.preOrderTraversal(node.right)

#     def postOrderTraversal(self, node):
#         if node:
#             self.postOrderTraversal(node.left)
#             self.postOrderTraversal(node.right)
#             print(node.data, end=" ")

#     def numberOfNodes(self, node):
#         if not node:
#             return 0
#         return 1 + self.numberOfNodes(node.left) + self.numberOfNodes(node.right)

#     def height(self, node):
#         if not node:
#             return -1
#         left_height = self.height(node.left)
#         right_height = self.height(node.right)
#         return 1 + max(left_height, right_height)

#     def isBST(self, node, min_val=float('-inf'), max_val=float('inf')):
#         if not node:
#             return True
#         if node.data < min_val or node.data > max_val:
#             return False
#         return self.isBST(node.left, min_val, node.data) and self.isBST(node.right, node.data, max_val)

#     def leafNodes(self, node):
#         if not node:
#             return
#         if not node.left and not node.right:
#             print(node.data, end=" ")
#         else:
#             self.leafNodes(node.left)
#             self.leafNodes(node.right)

#     def isSparseTree(self):
#         total_nodes = self.numberOfNodes(self.root)
#         leaf_nodes = self.numberOfLeafNodes(self.root)
#         return (leaf_nodes / total_nodes) < 0.5

#     def visualizeTree(self):
#         self._visualizeTree(self.root, 0)

#     def _visualizeTree(self, node, depth):
#         if not node:
#             return
#         self._visualizeTree(node.right, depth + 1)
#         print("    " * depth + str(node.data))
#         self._visualizeTree(node.left, depth + 1)

#     def minimum(self, node):
#         current = node
#         while current.left:
#             current = current.left
#         return current

#     def numberOfLeafNodes(self, node):
#         if not node:
#             return 0
#         if not node.left and not node.right:
#             return 1
#         return self.numberOfLeafNodes(node.left) + self.numberOfLeafNodes(node.right)

#     def isEmpty(self):
#         return self.root is None

#     def getTree(self):
#         return self.root

#     def __del__(self):
#         self.root = None
