class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1

def is_balanced(root):
    if root is None:
        return True
    if not is_balanced(root.left):
        return False
    if not is_balanced(root.right):
        return False
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1:
        return True
    else:
        return False

def is_balanced_with_height(root):
    if root is None:
        return True, 0
    balanced_left, lh = is_balanced_with_height(root.left)
    balanced_right, rh = is_balanced_with_height(root.right)
    current_height = max(lh, rh) + 1
    if abs(lh - rh) <= 1 and balanced_left and balanced_right:
        return True, current_height
    else:
        return False, current_height

# Main function
if __name__ == "__main__":
    # For balanced tree
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    # For unbalanced tree
    root2 = Node(1)
    root2.left = Node(2)
    root2.left.left = Node(3)

    # Using the is_balanced function
    if is_balanced(root2):
        print("Balanced Tree")
    else:
        print("Unbalanced Tree")

    # Using the is_balanced_with_height function
    balanced, tree_height = is_balanced_with_height(root2)
    if balanced:
        print("Balanced tree")
    else:
        print("Unbalanced tree")
