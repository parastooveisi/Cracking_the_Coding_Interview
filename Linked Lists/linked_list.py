class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = data if type(data) is Node else Node(data)

        if self.head is None:  # if the list is empty
            self.head = new_node
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = new_node
        new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev, data):
        new_node = Node(data)
        if not prev:
            print("Node not available")
            return
        new_node.next = prev.next
        prev.next = new_node

    def deletion(self, key):
        curr = self.head
        if curr.data == key:
            self.head = curr.next
            self.head = None
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if not curr:
            return

        prev.next = curr.next
        curr = None

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

    def list_length(self):
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next

        return count

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end="")
            if curr.next:
                print("-> ", end="")
            curr = curr.next
        print()
