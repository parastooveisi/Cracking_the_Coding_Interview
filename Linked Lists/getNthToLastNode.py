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

    def length(self):
        curr = self.head
        totalLen = 1

        while curr.next:
            totalLen += 1
            curr = curr.next

        return totalLen

    def nthToLastNode(self, n):

        curr = self.head
        length = self.length()

        while curr:
            if length == n:
                print(curr.data)
                return curr
            length -= 1
            curr = curr.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.nthToLastNode(4)
