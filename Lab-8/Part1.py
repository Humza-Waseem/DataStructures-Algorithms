class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insertNode(self,val):
        if(self.root == None):
            new_node = Node(val)
            self.root = new_node
        else:
            self.insertRecursive(val,self.root)
    def  insertRecursive(self,val,node):
        if(val < node.val):
            if (node.left is None):
                new_node = Node(val)
                node.left = new_node
            else:
                self.insertRecursive(val,node.left)
        elif(val > node.val):
            if(node.left is None):
                new_node = Node(val)
                node.right = new_node
            else:
                self.insertRecursive(val,node.left)
        
    def inOrderTraversal(self):
        first = self.root
        if(first is None):
            return None
        else:
            self.inOrderTraversal_recursive(self.root)
        print( "Root Value : ",self.root.val)

    def inOrderTraversal_recursive(self, node):
        if node != None:
            print(node.val, end=" ")
            self.inOrderTraversal_recursive(node.left)
            print(node.val, end=" ")
            self.inOrderTraversal_recursive(node.right)
            



    def isEmpty(self):
        return self.root== None
    
    def getTree(self):
        return self.root


a = BST()
a.insertNode(1)
a.insertNode(9)
a.insertNode(5)
a.insertNode(3)        
a.insertNode(4)        
a.insertNode(2)        

a.inOrderTraversal()


 


# class Node:
    
#     def __init__(data,parent,left,right):
#         self.data = data
#         self.parent = parent
#         self.left = None
#         self.right = None

    