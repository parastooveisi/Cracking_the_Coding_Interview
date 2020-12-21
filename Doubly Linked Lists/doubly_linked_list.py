class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = None
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
        new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = None
            return

        new_node.next = self.head
        self.head = new_node
        new_node.prev = None


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(2)
dllist.append(4)
dllist.append(5)
dllist.prepend(5)
dllist.prepend(7)

dllist.print_list()
