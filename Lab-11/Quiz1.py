class Node:
    def __init__(self, data, color='RED'):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = color


class RBTree:
    def __init__(self):
        self.NIL = Node(None, 'BLACK') 
        self.root = self.NIL

    def visualizeTree(self, node, level=0, prefix="Root: "):
        if node != self.NIL:
            print(' ' * (level * 4) + prefix + str(node.data) + ' (' + node.color + ')')
            self.visualizeTree(node.left, level + 1, 'L--- ')
            self.visualizeTree(node.right, level + 1, 'R--- ')

    def insert(self, value):
        node = Node(value)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'RED'

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'BLACK'
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == 'RED':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self._right_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = 'BLACK'

   
        
        

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y


# Example usage:
arr = [5, 3, 7, 1, 4, 6, 8]
rb_tree = RBTree()

for value in arr:
    rb_tree.insert(value)

rb_tree.visualizeTree(rb_tree.root)



















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

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
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
            return root  # because no duplicate nodes 

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        
        #left left 
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        #right right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # left right 
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # right left 
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
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
                temp = self.min_value_node(root.right)
                root.key = temp.key
                root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        # lft left 
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.rotate_right(root)

        # left Right 
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # right righ
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.rotate_left(root)

        # right left
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def visualize_tree_util(self, root, space):
        if root is None:
            return

        space += 5

        self.visualize_tree_util(root.right, space)

        print()
        for _ in range(5, space):
            print(" ", end=" ")

        print(root.key)

        self.visualize_tree_util(root.left, space)

    def visualize_tree(self):
        self.visualize_tree_util(self.root, 0)


if __name__ == "__main__":
    arr = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    avl_tree = AvlTree()          

    for key in arr:
        avl_tree.root = avl_tree.insert(avl_tree.root, key)

    print("AVL Tree Visualization:")
    avl_tree.visualize_tree()

    print("\nInserting 8...")
    avl_tree.root = avl_tree.insert(avl_tree.root, 8)
    avl_tree.visualize_tree()

    print("\nDeleting 10...")
    avl_tree.root = avl_tree.delete_node(avl_tree.root, 10)
    avl_tree.visualize_tree()
