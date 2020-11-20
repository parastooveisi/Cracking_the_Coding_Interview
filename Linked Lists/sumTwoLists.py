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

    def sumTwoLists(self, llist):
        p = self.head
        q = llist.head
        result = LinkedList()
        carry = 0

        while p or q:
            i = 0 if not p else p.data
            j = 0 if not q else q.data
            s = i + j + carry
            if s >= 10:
                carry = 1  # carry for the next round
                result.append(s % 10)

            else:
                carry = 0
                result.append(s)

            if p:
                p = p.next
            if q:
                q = q.next

        result.printList()


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)


llist.sumTwoLists(llist2)
