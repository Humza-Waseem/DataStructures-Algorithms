class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = color


class RBTree:
    def __init__(self):
        self.NIL = Node(None, 'black') 
        self.root = self.NIL


    def insert(self, value):
        node = Node(value)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'red'

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
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == 'red':

            if k.parent == k.parent.parent.right:

                u = k.parent.parent.left  # uncle

                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent

                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._right_rotate(k.parent.parent)


            if k == self.root:

                break

        self.root.color = 'black'