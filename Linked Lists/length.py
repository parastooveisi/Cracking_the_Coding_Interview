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

    def listLength(self):
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next

        return count


lList = LinkedList()
lList.append("A")
lList.append("B")
lList.printList()
lList.listLength()
