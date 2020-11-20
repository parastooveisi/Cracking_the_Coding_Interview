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

    def swap(self, keyA, keyB):

        if keyA == keyB:
            return

        prevA = prevB = None
        nodeA = nodeB = self.head

        while nodeA and nodeA.data != keyA:
            prevA = nodeA
            nodeA = nodeA.next

        while nodeB and nodeB.data != keyB:
            prevB = nodeB
            nodeB = nodeB.next

        if not nodeA or not nodeB:
            return

        if prevA:
            prevA.next = nodeB
        else:
            self.head = nodeB

        if prevB:
            prevB.next = nodeA
        else:
            self.head = nodeA

        nodeA.next, nodeB.next = nodeB.next, nodeA.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.printList()
llist.swap("B", "C")
llist.printList()
