class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AvlTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balanceFactor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # because,,,,, no duplicate nodes 

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balanceFactor(root)

        
        #left left 
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)   ## left k left pr right rotate hai

        #right right
        if balance < -1 and key > root.right.key:     # right right ------->  left rotate
            return self.leftRotate(root)

        # left right 
        if balance > 1 and key > root.left.key:          #   left k right ------> left rotate + right rotate
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # right left 
        if balance < -1 and key < root.right.key:      #     right k right ------>  right + left rotate
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


    def DeleteNode(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.DeleteNode(root.left, key)
        elif key > root.key:
            root.right = self.DeleteNode(root.right, key)
        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right

                if temp is None:
                    temp = root
                    root = None
                else:
                    root = temp

                del temp
            else:
                temp = self.minValueNode(root.right)
                root.key = temp.key
                root.right = self.DeleteNode(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balanceFactor(root)

        # lft left 
        if balance > 1 and self.balanceFactor(root.left) >= 0:
            return self.rightRotate(root)

        # left Right 
        if balance > 1 and self.balanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # right right
        if balance < -1 and self.balanceFactor(root.right) <= 0:
            return self.leftRotate(root)

        # right left
        if balance < -1 and self.balanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


