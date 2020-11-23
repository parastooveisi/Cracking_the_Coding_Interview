class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
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

    def is_cicular(self, input_list):
        curr = input_list.head
        while curr.next != input_list.head:
            curr = curr.next

        return curr.next == input_list.head


clist = CircularLinkedList()
clist.append("A")
clist.append("B")
clist.append("C")


clist.print_list()

print(clist.is_cicular(clist))
