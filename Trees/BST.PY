class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return Node(value)
    
    if value < root.data:
        root.left = insert_bst(root.left, value)
    else:
        # value > root.data
        root.right = insert_bst(root.right, value)
    
    return root

def inorder_traversal(root):
    if root is None:
        return
    
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

# Main function
if __name__ == "__main__":
    root = None
    root = insert_bst(root, 5)
    insert_bst(root, 4)
    insert_bst(root, 2)
    insert_bst(root, 7)
    insert_bst(root, 6)
    insert_bst(root, 1)

    # Print inorder
    inorder_traversal(root)
    print()
