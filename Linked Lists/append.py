class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def append(self, value):
        newNode = Node(value)

        if self.head is None:  # if the list is empty
            self.head = newNode
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = newNode


lList = LinkedList()
lList.append("A")
lList.append("B")
lList.printList()
