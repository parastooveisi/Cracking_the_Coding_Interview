class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True:
            if value > curr.data:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right

            elif value < curr.data:
                if not curr.left:
                    curr.left = new_node
                    break

                curr = curr.left

    def lookup(self, value):
        if not self.root:
            return False

        curr = self.root
        while curr:
            if value > curr.data:
                curr = curr.right
            elif value < curr.data:
                curr = curr.left
            elif value == curr.data:
                return True

        return False
