class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


def in_order_traversal(root):
    elements = []
    if root:
        elements = elements + in_order_traversal(root.left)
        elements.append(root.data)
        elements += in_order_traversal(root.right)

    return elements


def pre_order_traversal(root):
    elements = []
    if root:
        elements.append(root.data)
        elements += pre_order_traversal(root.left)
        elements += pre_order_traversal(root.right)

    return elements


def post_order_traversal(root):
    elements = []
    if root:
        elements += post_order_traversal(root.left)
        elements += post_order_traversal(root.right)
        elements.append(root.data)

    return elements
