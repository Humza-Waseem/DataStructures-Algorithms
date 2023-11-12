class Node:
    def __init__(self, data, color):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data, color):
        z = Node(data, color)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

        z.left = None
        z.right = None
        z.color = 'R'
        self._rb_insert_fixup(z)

    def _rb_insert_fixup(self, z):
        while z.parent is not None and z.parent.color == 'R':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y is not None and y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self._left_rotate(z.parent.parent)

        self.root.color = 'B'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
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

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def visualize_tree(self, node, space):
        if node is None:
            return

        space += 5
        self.visualize_tree(node.right, space)
        print()
        for i in range(5, space):
            print(" ", end=" ")

        print(f"{node.data} C:{node.color}")
        self.visualize_tree(node.left, space)


if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.insert(11, 'B')
    rb_tree.insert(14, 'B')
    rb_tree.insert(15, 'R')
    rb_tree.insert(2, 'R')
    rb_tree.insert(7, 'B')
    rb_tree.insert(1, 'B')
    rb_tree.insert(5, 'R')
    rb_tree.insert(8, 'R')
    rb_tree.insert(4, 'R')

    rb_tree.visualize_tree(rb_tree.root, 3)
