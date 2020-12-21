class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


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

    def add_after_node(self, key, data):
        new_node = Node(data)
        curr = self.head
        while curr.data != key:
            curr = curr.next

        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

    def add_before_node(self, key, data):
        new_node = Node(data)

        if key == self.head:
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node

        curr = self.head
        prev_node = None
        while curr.data != key:
            prev_node = curr
            curr = curr.next

        prev_node.next = new_node
        new_node.next = curr
        curr.prev = new_node
        new_node.prev = prev_node


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(2)
dllist.append(4)
dllist.print_list()
print("-------------------")
dllist.add_after_node(2, "B")
dllist.print_list()
print("-------------------")

dllist.add_before_node(4, "C")
dllist.print_list()
