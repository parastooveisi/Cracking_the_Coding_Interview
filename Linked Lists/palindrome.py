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

    def palindrome(self):
        hashMap = {}
        curr = self.head
        while curr:
            if curr.data in hashMap:
                hashMap[curr.data] += 1
            else:
                hashMap[curr.data] = 1

            curr = curr.next

        countOdds = 0
        for value in hashMap.values():
            if value % 2 != 0:
                countOdds += 1

        return countOdds <= 1


llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")
llist.append("R")


print(llist.palindrome())  # False
