class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return

        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
            return

        while cur.next != self.head:
            cur = cur.next

        cur.next = new_node
        self.head = new_node


c = CircularLinkedList()
c.append("A")
c.append("B")
c.prepend("C")
c.print_list()
