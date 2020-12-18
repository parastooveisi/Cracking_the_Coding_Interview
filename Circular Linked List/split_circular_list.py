# split A -> B -> C -> D in two separate circular lists
# A -> B -> and C -> D


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return

        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break

        return count

    def split_list(self):
        size = self.length()

        mid = size // 2
        count = 0
        prev = None
        curr = self.head

        while curr and count < mid:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = self.head

        clist = CircularLinkedList()
        while curr.next != self.head:
            clist.append(curr.data)
            curr = curr.next
        clist.append(curr.data)

        self.print_list()
        print("\n")
        clist.print_list()


c = CircularLinkedList()
c.append("A")
c.append("B")
c.append("C")
c.append("D")
c.split_list()
