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

    def remove_node(self, node):
        curr = self.head
        if self.head == node:
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            return

        prev = None
        while curr != node:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        curr = None

    def josephus_circle(self, step):

        if self.head is None:
            return

        curr = self.head
        count = 1
        while curr is not curr.next:
            if not count % step:
                print(curr.data, "REMOVED")
                self.remove_node(curr)
            curr = curr.next
            count += 1


clist = CircularList()
clist.append("A")
clist.append("B")
clist.append("C")
clist.append("D")

clist.josephus_circle(2)

clist.printList()
