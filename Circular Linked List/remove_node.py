class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def remove(self, key):
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
            return

        prev = None
        curr = self.head
        while curr.data != key:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        curr = None


clist = CircularList()
clist.append("A")
clist.append("B")
clist.append("C")

clist.printList()

clist.remove("B")

clist.remove("C")
clist.printList()
