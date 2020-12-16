# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
# Rotate on Node 4
# 5 -> 6 -> 1 -> 2 -> 3 -> 4


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return

        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

    def rotate(self, data):

        curr = self.head

        while curr.next:
            if curr.data == data:
                temp = curr
            curr = curr.next

        curr.next = self.head
        self.head = temp.next
        temp.next = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")

llist.rotate("B")

llist.printList()
