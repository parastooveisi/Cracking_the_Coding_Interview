class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def validate_BST(node, prev=None):
    if not node:
        return True

    if not validate_BST(node.left, prev):
        return False

    if prev and prev >= node.data:
        return False

    prev = node.data

    if not validate_BST(node.right, prev):
        return False

    return True


root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(4)
root.right.left.left = Node(40)
print(validate_BST(root))
