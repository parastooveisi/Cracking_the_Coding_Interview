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

    def delete_at_position(self, pos):

        if pos == 0:
            self.head = self.head.next
            return

        prev = None
        count = 1
        curr = self.head

        while curr and count != pos:
            prev = curr
            curr = curr.next
            count += 1

        if curr is None:
            return

        prev.next = curr.next
        curr = None


lList = LinkedList()
lList.append("A")
lList.append("B")
lList.append("C")
lList.append("D")
lList.append("E")

lList.delete_at_position(0)

lList.printList()
