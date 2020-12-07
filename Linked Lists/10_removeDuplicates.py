# Write code to remove duplicates from an unsorted linked list.


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

    def removeDuplicates(self):
        curr = self.head
        prev = None
        hashMap = dict()

        while curr:
            if curr.data in hashMap:
                prev.next = curr.next
                curr = None
            else:
                hashMap[curr.data] = 1
                prev = curr
            curr = prev.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(3)
llist.removeDuplicates()
llist.printList()
