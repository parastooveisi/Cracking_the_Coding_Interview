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

    def moveTailToHead(self):
        tail = self.head
        secondToTail = None

        while tail.next:
            secondToTail = tail
            tail = tail.next

        secondToTail.next = None
        tail.next = self.head
        self.head = tail


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.moveTailToHead()
llist.printList()
