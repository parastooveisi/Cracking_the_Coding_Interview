class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_balanced(node):
    if node is None:
        return 0
    left_height = is_balanced(node.left)
    if left_height == "NOT BALANCED":
        return "NOT BALANCED"
    right_height = is_balanced(node.right)
    if right_height == "NOT BALANCED":
        return "NOT BALANCED"
    diff = left_height - right_height
    if abs(diff) > 1:
        return "NOT BALANCED"
    return 1 + max(left_height, right_height)


root = Node(15)
root.left = Node(10)
root.right = Node(32)
root.left.left = Node(4)
root.left.right = Node(9)
root.left.left.left = Node(46)
root.left.left.right = Node(52)
print(is_balanced(root))
